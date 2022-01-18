import allure
from jsonschema import validate

def test_without_login_projects_check_status_code_equals_403(api_client): # незалогиненный пользователь должен получать ответ 403 при получении списка проектов
    response = api_client.get(path="/projects/", verify=False)
    assert response.status_code == 403

def test_login_projects_check_status_code_equals_200(get_login_token, api_client):  # залогиненный пользователь должен получать ответ 200 при получении списка проектов
    response = api_client.get(path="/projects/", headers={"authorization": get_login_token}, verify=False)
    assert response.status_code == 200
    print(response.json())


def test_login_project_check_status_code_equals_200(get_login_token, api_client, get_id_first_project):  # залогиненный пользователь должен получать ответ 200 при просмотре 1 проекта
    response = api_client.get(path="/projects/" + get_id_first_project, headers={"authorization": get_login_token}, verify=False)
    assert response.status_code == 200
    print(response.json())
def test_login_project_executors_check_status_code_equals_200(get_login_token, api_client, get_id_first_project):  # залогиненный пользователь должен получать ответ 200 при просмотре 1 проекта
    response = api_client.get(path="/projects/" + get_id_first_project, headers={"authorization": get_login_token}, verify=False)
    assert response.status_code == 200

def test_projects_check_content_type_equals_json(get_login_token, api_client): #проверка, что тело ответа в формат JSON
    response = api_client.get(path="/projects/", headers={"authorization": get_login_token}, verify=False)
    assert response.headers['Content-Type'] == "application/json"

def test_api_schema_projects(get_login_token, api_client):    # проверка схемы 1 проекта
    response = api_client.get(path="/projects/", headers={"authorization": get_login_token}, verify=False)
    schema = {
        "type": "object",
        "properties": {
            "id": {"type": "integer"},
            "uuid": {"type": "string"},
            "stage": {
                "type": "object",
                "properties": {
                    "uuid": {"type": "string"},
                    "name": {"type": ["string", "null"]},
                    "discription": {"type": ["string", "null"]}
                }
            },
            "status": {
                "type": "object",
                "properties": {
                    "uuid": {"type": "string"},
                    "name": {"type": ["string", "null"]},
                    "discription": {"type": ["string", "null"]}
                }
            },
            "customer": {
                "type": "object",
                "properties": {
                    "uuid": {"type": "string"},
                    "name": {"type": ["string", "null"]},
                    "discription": {"type": ["string", "null"]}
                }
            },
            "manager": {
                "type": "object",
                "properties": {
                    "uuid": {"type": "string"},
                    "status_uuid": {"type": ["string", "null"]},
                    "status_type": {"type": ["integer", "null"]},
                    "status_booking_type": {"type": ["string", "null"]},
                    "name": {"type": "string"},
                    "standard_rate": {"type": ["string", "null"]},
                    "overtime_rate": {"type": ["string", "null"]},
                    "code": {"type": ["string", "null"]},
                    "cost_per_use": {"type": ["string", "null"]},
                    "email_address": {"type": ["string", "null"]},
                    "initials": {"type": ["string", "null"]},
                    "material_label": {"type": ["string", "null"]},
                    "group": {"type": ["string", "null"]},
                    "max_units": {"type": ["string", "null"]},
                    "timesheet_manager_uid": {"type": ["string", "null"]},
                    "available_from": {"type": ["string", "null"]},
                    "available_to": {"type": ["string", "null"]},
                    "can_level": {"type": "boolean"},
                    "hyperlink": {"type": ["string", "null"]},
                    "hyperlink_href": {"type": ["string", "null"]},
                    "nt_account": {"type": ["string", "null"]},
                    "claims_account": {"type": ["string", "null"]},
                    "is_active": {"type": "boolean"},
                    "is_generic": {"type": "boolean"},
                    "is_team": {"type": "boolean"},
                    "base_calendar": {"type": ["string", "null"]},
                    "workgroup": {"type": ["string", "null"]},
                    "client_id": {"type": "integer"},
                    "cost_center": {"type": ["string", "null"]},
                    "created_revision_counter": {"type": "integer"},
                    "modified_revision_counter": {"type": "integer"},
                    "created_date": {"type": "string"},
                    "modified_date": {"type": "string"},
                    "count": {"type": "integer"},
                    "sd_res": {"type": ["string", "null"]},
                    "cost_type": {"type": ["string", "null"]},
                    "dept": {"type": ["string", "null"]},
                    "role": {"type": ["string", "null"]}
                }
            },
            "object_type": {
                "type": ["object", "null"],
                "properties": {
                    "uuid": {"type": "string"},
                    "name": {"type": ["string", "null"]},
                    "discription": {"type": ["string", "null"]}
                }
            },
            "code": {"type": ["string", "null"]},
            "name": {"type": "string"},
            "project_type": {"type": "string"},
            "address": {"type": ["string", "null"]},
            "area": {"type": ["number", "null"]},
            "object_type_name": {"type": ["string", "null"]}
        }
    }
    validate(instance=response.json()[1], schema=schema)

def test_create_project_check_status_code_equals_201(get_login_token, api_client): #проверка создания проекта под залогиненным пользователем, должны получить ответ 201
    data = {
        "uuid": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "code": "ПТ-РЕК-57А",
        "name": "Тестовый проект 1231",
        "project_type": "d0c6743e-5fa5-e511-9420-005056ae5a80",
        "address": "Рвпрывпр,1232456",
        "area": 1000,
        "object_type_name": "ТЦ",
        "stage": "3a2a1993-baa7-e511-9423-005056ae5a80",
        "status": "47ec10fe-fbf7-e511-9446-005056a7072a",
        "customer": "5932e8c3-5fa5-e511-9420-005056ae5a80",
        "manager": "5a0a4688-91ac-e611-9431-005056ae00ac",
        "object_type": "4553d1d4-bea7-e511-9423-005056ae5a80"
    }
    response = api_client.post(path="/projects/", headers={"authorization": get_login_token}, verify=False, data = data)
#    assert response.status_code == 201
    print(response.json())

