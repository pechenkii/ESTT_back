import allure
from jsonschema import validate
import datetime

def test_without_login_photo_check_status_code_equals_403(api_client, get_id_last_foto): # незалогиненный пользователь должен получать ответ 403 при получении определенной фото
    response = api_client.get(path="/photos/" + get_id_last_foto + "/", verify=False)
    assert response.status_code == 403


def test_login_photo_check_status_code_equals_200(get_login_token, api_client, get_id_last_foto): # залогиненный пользователь должен получать ответ 200 при получении определенной фото
    response = api_client.get(path="/photos/" + get_id_last_foto + "/", headers={"authorization": get_login_token}, verify=False)
    assert response.status_code == 200
    print(response.json())


def test_photo_check_content_type_equals_json(get_login_token, api_client, get_id_last_foto): #проверка, что тело ответа в формат JSON
    response = api_client.get(path="/photos/" + get_id_last_foto + "/", headers={"authorization": get_login_token}, verify=False)
    assert response.headers['Content-Type'] == "application/json"

def test_api_schema_photo(get_login_token, api_client, get_id_last_foto):    # проверка схемы 1 фото
    response = api_client.get(path="/photos/" + get_id_last_foto + "/", headers={"authorization": get_login_token}, verify=False)
    schema = {
        "type": "object",
        "properties": {
            "id": {"type": "integer"},
            "image_date": {"type": "string"},
            "image_file": {"type": "string"},
            "comment": {"type": ["string", "null"]},
            "show_in_reports": {"type": "boolean"},
            "timestamp": {"type": "string"},
            "project": {"type": "integer"}
        }
    }
    validate(instance=response.json(), schema=schema)

def test_change_photo_check_status_code_equals_200(get_login_token, api_client, get_id_last_foto): # проверка изменения фото полностью
    files = {"image_file": open("/Users/evgen/Documents/foto_1.png", "rb")}
    data = {
        "image_file": "foto_1.png",
        "image_date": datetime.date.today(),
        "comment": "новый комментарий",
        "show_in_reports": False
    }
    response = api_client.put(path="/photos/" + get_id_last_foto + "/", headers={"authorization": get_login_token}, verify=False, data=data, files=files)
    assert response.status_code == 200
    print(response.json())

def test_change_data_photo_check_status_code_equals_201(get_login_token, api_client, get_id_last_foto): # проверка изменения комментария к фото
    files = {"image_file": open("/Users/evgen/Documents/foto_1.png", "rb")}
    data = {
#        "image_file": "foto_1.png",
#        "image_date": datetime.date.today(),
        "comment": "Изменен только комментарий комментарий и показ в отчете",
#        "show_in_reports": True
    }
    response = api_client.patch("/photos/" + get_id_last_foto + "/", headers={"authorization": get_login_token}, verify=False, data=data, files=files)
    assert response.status_code == 200
    print(response.json())

def test_delete_photo_check_status_code_equals_204(get_login_token, get_id_last_foto, api_client): #проверка удаления фото залогиненным пользователем, должны получить ответ 204
    response = api_client.delete(path="/photos/" + get_id_last_foto + "/", headers={"authorization": get_login_token}, verify=False)
    assert response.status_code == 204
