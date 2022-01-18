import allure
from jsonschema import validate

def test_without_login_customers_check_status_code_equals_403(api_client):    # незалогиненный пользователь должен получать ответ 403 при получении списка заказчиков
    response = api_client.get(path="/customers/", verify=False)
    assert response.status_code == 403

def test_login_customers_check_status_code_equals_200(get_login_token, api_client): # залогиненный пользователь должен получать ответ 200 при получении списка заказчиков
    response = api_client.get(path="/customers/", headers={"authorization": get_login_token}, verify=False)
    assert response.status_code == 200

def test_customers_check_content_type_equals_json(get_login_token, api_client): #проверка, что тело ответа в формат JSON
    response = api_client.get(path="/customers/", headers={"authorization": get_login_token}, verify=False)
    assert response.headers['Content-Type'] == "application/json"

def test_api_schema_customers(get_login_token, api_client):    # проверка схемы страницы заказчиков
    response = api_client.get(path="/customers/", headers={"authorization": get_login_token}, verify=False)
    schema = {
        "type": "object",
        "properties": {
            "uuid": {"type": "string"},
            "name": {"type": ["string", "null"]},
            "discription": {"type": ["string", "null"]}
        }
    }
    validate(instance=response.json()[2], schema=schema)

def test_sdf(get_id_first_project):
    print(get_id_first_project)