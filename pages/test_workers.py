import allure
from jsonschema import validate

def test_without_login_workers_check_status_code_equals_403(api_client): # незалогиненный пользователь должен получать ответ 403 при получении списка показателей
    response = api_client.get(path="/workers/", verify=False)
    assert response.status_code == 403

def test_login_workers_check_status_code_equals_200(get_login_token, api_client): # залогиненный пользователь должен получать ответ 200 при получении списка показателей
    response = api_client.get(path="/workers/", headers={"authorization": get_login_token}, verify=False)
    assert response.status_code == 200


def test_login_workers_with_param_check_status_code_equals_200(get_login_token, api_client): # залогиненный пользователь должен получать ответ 200 при получении списка показателей по определенным параметрам
    response = api_client.get(path="/workers/", headers={"authorization": get_login_token}, verify=False, params={'is_active': True, 'name': 'Рабочие'})
    assert response.status_code == 200

def test_workers_check_content_type_equals_json(get_login_token, api_client): #проверка, что тело ответа в формат JSON
    response = api_client.get(path="/workers/", headers={"authorization": get_login_token}, verify=False)
    assert response.headers['Content-Type'] == "application/json"

def test_api_schema_workers(get_login_token, api_client):    # проверка схемы 1 показателя
    response = api_client.get(path="/workers/", headers={"authorization": get_login_token}, verify=False)
    schema = {
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
    }
    validate(instance=response.json()[1], schema=schema)