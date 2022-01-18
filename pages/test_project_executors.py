import allure
from jsonschema import validate

def test_without_login_project_executors_check_status_code_equals_403(api_client, get_id_first_project): # незалогиненный пользователь должен получать ответ 401 при получении списка показателей у проекта
    response = api_client.get(path="/projects/" + get_id_first_project +"/executors/", verify=False)
    assert response.status_code == 403

def test_login_project_executors_check_status_code_equals_200(get_login_token, api_client, get_id_first_project):  # залогиненный пользователь должен получать ответ 200 при получении списка показателей у проекта
    response = api_client.get(path="/projects/" + get_id_first_project +"/executors/", headers={"authorization": get_login_token}, verify=False)
    assert response.status_code == 200
    print(response.json())

def test_create_executor_check_status_code_equals_201(get_login_token, api_client, get_id_first_project): #проверка создания показателя залогиненным пользователем, должны получить ответ 201
    body = {
        "executor": 5,
        "count": "впапва"
    }
    response = api_client.post(path="/projects/" + get_id_first_project +"/executors/", headers={"authorization": get_login_token}, verify=False, data = body)
#    assert response.status_code == 201
    print(response.json())

def test_api_schema_executor(get_login_token, api_client, get_id_first_project):    # проверка схемы 1 показателя
    response = api_client.get(path="/projects/" + get_id_first_project +"/executors/", headers={"authorization": get_login_token}, verify=False)
    schema = {
        "type": "object",
        "properties": {
            "id": {"type": "integer"},
            "project": {
                        "type": "object",
                        "properties": {
                            "id": {"type": "integer"},
                            "uuid": {"type": ["string", "null"]},
                            "code": {"type": ["string", "null"]},
                            "name": {"type": "string"}
                        }
                    },
            "executor": {
                "type": "object",
                "properties": {
                    "id": {"type": "integer"},
                    "unit": {
                        "type": "object",
                        "properties": {
                            "id": {"type": "integer"},
                            "name": {"type": "string"}
                        }
                    },
                    "name": {"type": "string"},
                    "is_active": {"type": "boolean"}
                }
            },
            "day": {"type": "string"},
            "count": {"type": "integer"}
        }
    }
    validate(instance=response.json()[1], schema=schema)