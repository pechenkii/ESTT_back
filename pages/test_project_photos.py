import allure
import datetime

def test_without_login_projects_photos_check_status_code_equals_403(api_client, get_id_first_project): # незалогиненный пользователь должен получать ответ 403 при получении списка фото проекта
    response = api_client.get(path="/projects/" + get_id_first_project + "/photos/", verify=False)
    assert response.status_code == 403

def test_login_projects_photos_check_status_code_equals_200(get_login_token, api_client, get_id_first_project): # залогиненный пользователь должен получать ответ 200 при получении списка фото проекта
    response = api_client.get(path="/projects/" + get_id_first_project + "/photos/", headers={"authorization": get_login_token}, verify=False)
    assert response.status_code == 200
    print(response.json())

def test_create_projects_photos_check_status_code_equals_201(get_login_token, api_client, get_id_first_project): # проверка добавления 1 фото к проекту
    files = {"image_file": open("/Users/evgen/Documents/foto.png", "rb")}
    body = {
        "image_file": "foto.png",
        "image_date": datetime.date.today(),
        "comment": "123",
        "show_in_reports": True
    }
    response = api_client.post(path="/projects/" + get_id_first_project + "/photos/", headers={"authorization": get_login_token}, verify=False, data=body, files=files)
    assert response.status_code == 201
    print(response.json())
