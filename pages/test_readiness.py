import allure
from jsonschema import validate

def test_without_login_readiness_check_status_code_equals_200(api_client): # незалогиненный пользователь должен получать ответ 200 при получении ответа от readiness
    response = api_client.get(path="/readiness/", verify=False)
    assert response.status_code == 200

def test_readiness_check_content_type_equals_json(api_client): #проверка, что тело ответа в формат JSON
    response = api_client.get(path="/readiness/", verify=False)
    assert response.headers['Content-Type'] == "application/json"

def test_readiness_check_result_equals_True(api_client):   #
    response = api_client.get(path="/readiness/", verify=False)
    response_body = response.json()
    assert response_body["result"] == True

def test_readiness_check_db_equals_True(api_client):   #
    response = api_client.get(path="/readiness/", verify=False)
    response_body = response.json()
    assert response_body["services"]["db"] == True

def test_readiness_check_s3_equals_True(api_client):   #
    response = api_client.get(path="/readiness/", verify=False)
    response_body = response.json()
    assert response_body["services"]["s3"] == True

def test_readiness_check_keycloak_equals_True(api_client):   #
    response = api_client.get(path="/readiness/", verify=False)
    response_body = response.json()
    assert response_body["services"]["keycloak"] == True

def test_api_schema_readiness(api_client):    # проверка схемы страницы readiness
    response = api_client.get(path="/readiness/", verify=False)
    schema = {
        "type": "object",
        "properties": {
            "result": {"type": "boolean"},
            "services": {
                "type": "object",
                "properties": {
                    "db": {"type": "boolean"},
                    "s3": {"type": "boolean"},
                    "keycloak": {"type": "boolean"}
                }
            }
        }
    }
    validate(instance=response.json(), schema=schema)

