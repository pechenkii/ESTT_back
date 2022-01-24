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

def test_without_login_projects_estimate_files_check_status_code_equals_403(api_client, get_id_first_project): # незалогиненный пользователь должен получать ответ 403 при получении файлов сметыv проекта
    response = api_client.get(path="/projects/" + get_id_first_project + "/estimate-files", verify=False)
    assert response.status_code == 403

def test_login_projects_estimate_files_check_status_code_equals_200(get_login_token, api_client, get_id_first_project): # залогиненный пользователь должен получать ответ 200 при получении файлов сметы проекта
    response = api_client.get(path="/projects/" + get_id_first_project + "/estimate-files", headers={"authorization": get_login_token}, verify=False)
    assert response.status_code == 200
    print(response.json())

def test_create_projects_estimate_file_check_status_code_equals_201(get_login_token, api_client, get_id_first_project): # проверка добавления файла сметы к проекту
    files = {"xls_file": open("/Users/evgen/Documents/file.xlsx", "rb")}
    data = {
        "xls_file": "file.xlsx",
        "active_since": datetime.datetime.now() + datetime.timedelta(seconds=2)
    }
    response = api_client.post(path="/projects/" + get_id_first_project + "/estimate-files", headers={"authorization": get_login_token}, verify=False, data=data, files=files)
    assert response.status_code == 201

def test_api_schema_estimate_file(get_login_token, api_client, get_id_first_project):    # проверка схемы файла сметы
    response = api_client.get(path="/projects/" + get_id_first_project + "/estimate-files", headers={"authorization": get_login_token}, verify=False)
    schema = {
        "type": "object",
        "properties": {
            "id": {"type": "integer"},
            "project_id": {"type": "integer"},
            "xls_file": {"type": "string"},
            "active_since": {"type": "string"},
            "processed_at": {"type": ["string", "null"]},
#            "processed_at": {"type": "string"},
            "process_status": {"type": "string"},
            "owner_id": {"type": "integer"},
            "created_at": {"type": "string"}
        }
    }
    validate(instance=response.json()[1], schema=schema)
#    print(response.json()[1])

def test_without_login_projects_estimate_file_events_check_status_code_equals_403(api_client, get_id_first_project, get_id_last_estimate_file): # незалогиненный пользователь должен получать ответ 403 при получении списка ошибок в файле сметы
    response = api_client.get(path="/projects/" + get_id_first_project + "/estimate-files/" + get_id_last_estimate_file + "/events", verify=False)
    assert response.status_code == 403

def test_login_projects_estimate_file_events_check_status_code_equals_200(get_login_token, api_client, get_id_first_project, get_id_last_estimate_file): # залогиненный пользователь должен получать ответ 200 при получении списка ошибок в файле сметы
    response = api_client.get(path="/projects/" + get_id_first_project + "/estimate-files/" + get_id_last_estimate_file + "/events", headers={"authorization": get_login_token}, verify=False)
    assert response.status_code == 200
    print(response.json())

def test_login_projects_estimate_rows_check_status_code_equals_200(get_login_token, api_client, get_id_first_project, get_id_last_estimate_file): # залогиненный пользователь должен получать ответ 200 при получении списка строк сметы проекта
    response = api_client.get(path="/projects/" + get_id_first_project + "/estimate-files/" + get_id_last_estimate_file + "/rows", headers={"authorization": get_login_token}, verify=False)
    assert response.status_code == 200
    print(response.json())

def test_create_estimate_file_row_check_status_code_equals_201(get_login_token, api_client, get_id_first_project, get_id_last_estimate_file): # проверка создания строки сметы залогиненным пользователем, должны получить ответ 201
    data = {
        "name": "Строка",
        "hierarchy_number": 5,
        "measure_name": "Тестовая строка",
        "count_plan": 1,
        "count_fact": 1,
        "price_work": 1,
        "price_material": 1,
        "estimate_file": 1
    }
    response = api_client.post(path="/projects/" + get_id_first_project + "/estimate-files/" + get_id_last_estimate_file + "/rows", headers={"authorization": get_login_token}, verify=False, data = data)
    assert response.status_code == 201
    print(response.json())

def test_second_create_estimate_file_row_check_status_code_equals_201(get_login_token, api_client, get_id_first_project, get_id_last_estimate_file): # проверка повторного создания такой же строки сметы залогиненным пользователем, должны получить ответ 400
    data = {
        "name": "Строка",
        "hierarchy_number": 5,
        "measure_name": "Тестовая строка-дубль",
        "count_plan": 1,
        "count_fact": 1,
        "price_work": 1,
        "price_material": 1,
        "estimate_file": 1
    }
    response = api_client.post(path="/projects/" + get_id_first_project + "/estimate-files/" + get_id_last_estimate_file + "/rows", headers={"authorization": get_login_token}, verify=False, data = data)
    assert response.status_code == 400

#/projects/1/estimate-files/1/rows-today-values

def test_without_login_projects_estimate_rows_today_values_check_status_code_equals_403(get_login_token, api_client, get_id_first_project, get_id_last_estimate_file,get_id_last_estimate_file_row): # незалогиненный пользователь должен получать ответ 403 при получении текущего значения всех строк сметы
    response = api_client.get(path="/projects/" + get_id_first_project + "/estimate-files/" + get_id_last_estimate_file + "/rows-today-values", verify=False)
    assert response.status_code == 403

def test_login_projects_estimate_rows_today_values_check_status_code_equals_equals_200(get_login_token, api_client, get_id_first_project, get_id_last_estimate_file,get_id_last_estimate_file_row): # залогиненный пользователь должен получать ответ 200 при получении текущего значения всех строк сметы
    response = api_client.get(path="/projects/" + get_id_first_project + "/estimate-files/" + get_id_last_estimate_file + "/rows-today-values", headers={"authorization": get_login_token}, verify=False)
    assert response.status_code == 200
    print(response.json())


def test_1(get_id_last_estimate_file_row):
    print(get_id_last_estimate_file_row)

#доделать
def test_create_estimate_file_row_check_status_code_equals_201(get_login_token, api_client, get_id_first_project, get_id_last_estimate_file, get_id_last_estimate_file_row): # проверка создания значения на сегодня в строке сметы залогиненным пользователем, должны получить ответ 201
    data = {
        "records": [{"row_id": 14888, "value": 10}]
        }
    response = api_client.post(path="/projects/" + get_id_first_project + "/estimate-files/" + get_id_last_estimate_file + "/rows-today-values/bulk", headers={"authorization": get_login_token}, verify=False, data = data)
#    assert response.status_code == 201
    print(response.json())


def test_without_login_projects_estimate_row_check_status_code_equals_403(get_login_token, api_client, get_id_first_project, get_id_last_estimate_file,get_id_last_estimate_file_row): # незалогиненный пользователь должен получать ответ 403 при получении строки сметы проекта
    response = api_client.get(path="/projects/" + get_id_first_project + "/estimate-files/" + get_id_last_estimate_file + "/rows/" + get_id_last_estimate_file_row, verify=False)
    assert response.status_code == 403

def test_login_projects_estimate_row_check_status_code_equals_200(get_login_token, api_client, get_id_first_project, get_id_last_estimate_file,get_id_last_estimate_file_row): # залогиненный пользователь должен получать ответ 200 при получении строки сметы проекта
    response = api_client.get(path="/projects/" + get_id_first_project + "/estimate-files/" + get_id_last_estimate_file + "/rows/" + get_id_last_estimate_file_row, headers={"authorization": get_login_token}, verify=False)
    assert response.status_code == 200
    print(response.json())

def test_login_change_projects_estimate_row_check_status_code_equals_200(get_login_token, api_client, get_id_first_project, get_id_last_estimate_file,get_id_last_estimate_file_row): # залогиненный пользователь должен получать ответ 200 при изменении строки сметы проекта
    data = {
        "name": "Тестовые работы 2.0",
        "hierarchy_number": "3.4.3",
        "measure_name": "кк",
        "count_plan": "7000",
        "count_fact_initial": 0,
        "price_work": 100,
        "price_material": 50
    }
    response = api_client.put(path="/projects/" + get_id_first_project + "/estimate-files/" + get_id_last_estimate_file + "/rows/" + get_id_last_estimate_file_row, headers={"authorization": get_login_token}, verify=False, data = data)
    assert response.status_code == 200

def test_login_delete_projects_estimate_row_check_status_code_equals_200(get_login_token, api_client, get_id_first_project, get_id_last_estimate_file,get_id_last_estimate_file_row): # залогиненный пользователь должен получать ответ 204 при удалении строки сметы проекта
    response = api_client.delete(path="/projects/" + get_id_first_project + "/estimate-files/" + get_id_last_estimate_file + "/rows/" + get_id_last_estimate_file_row, headers={"authorization": get_login_token}, verify=False)
    assert response.status_code == 204

def test_without_login_projects_estimate_file_check_status_code_equals_403(api_client, get_id_first_project, get_id_last_estimate_file): # незалогиненный пользователь должен получать ответ 403 при получении определенного файла сметы проекта
    response = api_client.get(path="/projects/" + get_id_first_project + "/estimate-files/" + get_id_last_estimate_file, verify=False)
    assert response.status_code == 403

def test_login_projects_estimate_file_check_status_code_equals_200(get_login_token, api_client, get_id_first_project, get_id_last_estimate_file): # залогиненный пользователь должен получать ответ 200 при получении определенного файла сметы проекта
    response = api_client.get(path="/projects/" + get_id_first_project + "/estimate-files/" + get_id_last_estimate_file, headers={"authorization": get_login_token}, verify=False)
    assert response.status_code == 200
    print(response.json())

def test_delete_estimate_file_value_check_status_code_equals_204(get_login_token, api_client, get_id_first_project, get_id_last_estimate_file): # проверка удаления файла сметы залогиненным пользователем, должны получить ответ 204
    response = api_client.delete(path="/projects/" + get_id_first_project + "/estimate-files/" + get_id_last_estimate_file, headers={"authorization": get_login_token}, verify=False)
    assert response.status_code == 204

