import allure
from jsonschema import validate

def test_without_login_users_check_status_code_equals_403(api_client): # незалогиненный пользователь должен получать ответ 403 при получении списка пользователей
    response = api_client.get(path="/users/", verify=False)
    assert response.status_code == 403

def test_login_users_check_status_code_equals_200(get_login_token, api_client): # залогиненный пользователь должен получать ответ 200 при получении списка пользователей
    response = api_client.get(path="/users/", headers={"authorization": get_login_token}, verify=False)
    assert response.status_code == 200
    print(response.json())

def test_users_check_content_type_equals_json(get_login_token, api_client): #проверка, что тело ответа в формат JSON
    response = api_client.get(path="/users/", headers={"authorization": get_login_token}, verify=False)
    assert response.headers['Content-Type'] == "application/json"

def test_api_schema_users(get_login_token, api_client):    # проверка схемы страницы users
    response = api_client.get(path="/users/", headers={"authorization": get_login_token}, verify=False)
    schema = {
        "type": "object",
        "properties": {
            "id": {"type": "integer"},
            "first_name": {"type": "string"},
            "last_name": {"type": "string"},
            "email": {"type": "string"}
        }
    }
    validate(instance=response.json()[2], schema=schema)