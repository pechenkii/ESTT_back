import allure
from jsonschema import validate

def test_without_login_employees_check_status_code_equals_403(api_client):    # незалогиненный пользователь должен получать ответ 403 при получении списка исполнителей
    response = api_client.get(path="/employees/", verify=False)
    assert response.status_code == 403

def test_login_employees_check_status_code_equals_200(get_login_token, api_client): # залогиненный пользователь должен получать ответ 200 при получении списка исполнителей
    response = api_client.get(path="/employees/", headers={"authorization": get_login_token}, verify=False)
    assert response.status_code == 200


def test_employees_check_content_type_equals_json(get_login_token, api_client): #проверка, что тело ответа в формат JSON
    response = api_client.get(path="/employees/", headers={"authorization": get_login_token}, verify=False)
    assert response.headers['Content-Type'] == "application/json"

def test_api_schema_employees(get_login_token, api_client):    # проверка схемы страницы исполнителя
    response = api_client.get(path="/employees/", headers={"authorization": get_login_token}, verify=False)
    schema = {
        "type": "object",
        "properties": {
            "uuid": {"type": "string"},
            "status_uuid": {"type": ["string", "null"]},
            "status_type": {"type": ["integer", "null"]},
            "status_booking_type": {"type": ["string", "null"]},
            "name": {"type": "string"},
            "standart_rate": {"type": ["string", "null"]},
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
            "modified_date": {"type": ["string", "null"]},
            "count": {"type": "integer"},
            "sd_res": {"type": ["string", "null"]},
            "cost_type": {"type": ["string", "null"]},
            "dept": {"type": ["string", "null"]},
            "role": {"type": ["string", "null"]}
        }
    }
    validate(instance=response.json()[1], schema=schema)