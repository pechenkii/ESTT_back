import allure
from jsonschema import validate

def test_without_login_stages_check_status_code_equals_403(api_client):    # незалогиненный пользователь должен получать ответ 403 при получении списка этапов
    response = api_client.get(path="/project_stages/", verify=False)
    assert response.status_code == 403

def test_login_stages_check_status_code_equals_200(get_login_token, api_client): # залогиненный пользователь должен получать ответ 200 при получении списка этапов
    response = api_client.get(path="/project_stages/", headers={"authorization": get_login_token}, verify=False)
    assert response.status_code == 200

def test_stages_check_content_type_equals_json(get_login_token, api_client): #проверка, что тело ответа в формат JSON
    response = api_client.get(path="/project_stages/", headers={"authorization": get_login_token}, verify=False)
    assert response.headers['Content-Type'] == "application/json"

def test_api_schema_stage(get_login_token, api_client):    # проверка схемы 1 типа этапа
    response = api_client.get(path="/project_stages/", headers={"authorization": get_login_token}, verify=False)
    schema = {
        "type": "object",
        "properties": {
            "uuid": {"type": "string"},
            "name": {"type": ["string", "null"]},
            "discription": {"type": ["string", "null"]}
        }
    }
    validate(instance=response.json()[1], schema=schema)