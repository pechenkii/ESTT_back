import allure
import datetime
from jsonschema import validate


def test_without_login_project_active_estimate_file_check_status_code_equals_403(api_client, get_id_first_project): # незалогиненный пользователь должен получать ответ 403 при получении активного файла сметы проекта
    response = api_client.get(path="/projects/" + get_id_first_project + "/active-estimate-file", verify=False)
    assert response.status_code == 403

def test_login_project_active_estimate_file_check_status_code_equals_200(get_login_token, api_client, get_id_first_project): # залогиненный пользователь должен получать ответ 200 при получении активного файла сметы проекта
    response = api_client.get(path="/projects/" + get_id_first_project + "/active-estimate-file", headers={"authorization": get_login_token}, verify=False)
    assert response.status_code == 200
    print(response.json())

def test_without_login_projects_estimate_rows_check_status_code_equals_403(api_client, get_id_first_project): # незалогиненный пользователь должен получать ответ 403 при получении списка активных строк файла сметы проекта
    response = api_client.get(path="/projects/" + get_id_first_project + "/active-estimate-rows", verify=False)
    assert response.status_code == 403

def test_login_projects_estimate_rows_check_status_code_equals_200(get_login_token, api_client, get_id_first_project): # залогиненный пользователь должен получать ответ 200 при получении списка активных строк файла сметы проекта
    response = api_client.get(path="/projects/" + get_id_first_project + "/active-estimate-rows", headers={"authorization": get_login_token}, verify=False)
    assert response.status_code == 200
    print(response.json())

def test_without_login_projects_estimate_file_check_status_code_equals_403(api_client, get_id_first_project): # незалогиненный пользователь должен получать ответ 403 при получении файла сметыv проекта
    response = api_client.get(path="/projects/" + get_id_first_project + "/estimate-files", verify=False)
    assert response.status_code == 403

def test_login_projects_estimate_file_check_status_code_equals_200(get_login_token, api_client, get_id_first_project): # залогиненный пользователь должен получать ответ 200 при получении файла сметы проекта
    response = api_client.get(path="/projects/" + get_id_first_project + "/estimate-files", headers={"authorization": get_login_token}, verify=False)
    assert response.status_code == 200
    print(response.json())

def test_create_projects_estimate_file_check_status_code_equals_201(get_login_token, api_client, get_id_first_project): # проверка добавления файла сметы к проекту
    files = {"xls_file": open("/Users/evgen/Documents/file.xlsx", "rb")}
    body = {
        "xls_file": "file.xlsx",
#        "active_since": datetime.datetime.now()
        "active_since": "2022-01-17 10:30:50.648998"

    }
    response = api_client.post(path="/projects/" + get_id_first_project + "/estimate-files", headers={"authorization": get_login_token}, verify=False, data=body, files=files)
#    assert response.status_code == 201
    print(response.json())
    print(datetime.datetime.now())

def test_api_schema_roles(get_login_token, api_client, get_id_first_project):    # проверка схемы страницы ролей (ждем появления точки обратно)
    response = api_client.get(path="/projects/" + get_id_first_project + "/estimate-files", headers={"authorization": get_login_token}, verify=False)
    schema = {
        "type": "object",
        "properties": {
            "id": {"type": "integer"},
            "project_id": {"type": "integer"},
            "xls_file": {"type": "string"},
            "active_since": {"type": "string"},
#            "processed_at": {"type": ["string", "null"]},
            "processed_at": {"type": "string"},
            "process_status": {"type": "string"},
            "owner_id": {"type": "integer"},
            "created_at": {"type": "string"}
        }
    }
    validate(instance=response.json()[1], schema=schema)
#    print(response.json()[1])

def test_login_projects_estimate_rows_check_status_code_equals_200(get_login_token, api_client, get_id_first_project, get_id_last_estimate_file): # залогиненный пользователь должен получать ответ 200 при получении списка строк сметы проекта
    response = api_client.get(path="/projects/" + get_id_first_project + "/estimate-files/" + get_id_last_estimate_file + "/rows", headers={"authorization": get_login_token}, verify=False)
    assert response.status_code == 200
    print(response.json())

def test_create_estimate_file_row_check_status_code_equals_201(get_login_token, api_client, get_id_first_project, get_id_last_estimate_file): # проверка создания строки сметы залогиненным пользователем, должны получить ответ 201
    data = {
        "name": "Строка",
        "hierarchy_number": 5,
        "measure_name": "ыыфвыв",
        "count_plan": 1,
        "count_fact": 1,
        "price_work": 1,
        "price_material": 1,
        "estimate_file": 1
    }
    response = api_client.post(path="/projects/" + get_id_first_project + "/estimate-files/" + get_id_last_estimate_file + "/rows", headers={"authorization": get_login_token}, verify=False, data = data)
    assert response.status_code == 201
    print(response.json())

def test_122(get_id_last_estimate_file_row):
    print(get_id_last_estimate_file_row)

def test_login_projects_estimate_row_check_status_code_equals_200(get_login_token, api_client, get_id_first_project, get_id_last_estimate_file,get_id_last_estimate_file_row): # залогиненный пользователь должен получать ответ 200 при получении строки сметы проекта
    response = api_client.get(path="/projects/" + get_id_first_project + "/estimate-files/" + get_id_last_estimate_file + "/rows/" + get_id_last_estimate_file_row, headers={"authorization": get_login_token}, verify=False)
    assert response.status_code == 200
    print(response.json())

def test_login_delete_projects_estimate_row_check_status_code_equals_200(get_login_token, api_client, get_id_first_project, get_id_last_estimate_file,get_id_last_estimate_file_row): # залогиненный пользователь должен получать ответ 204 при удалении строки сметы проекта
    response = api_client.delete(path="/projects/" + get_id_first_project + "/estimate-files/" + get_id_last_estimate_file + "/rows/" + get_id_last_estimate_file_row, headers={"authorization": get_login_token}, verify=False)
    assert response.status_code == 204
#    print(response.json())