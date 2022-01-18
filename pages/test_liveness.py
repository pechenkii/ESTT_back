import allure
from jsonschema import validate

def test_without_login_liveness_check_status_code_equals_200(api_client): # незалогиненный пользователь должен получать ответ 200 при получении ответа от liveness
    response = api_client.get(path="/liveness/", verify=False)
    assert response.status_code == 200

def test_liveness_check_content_type_equals_json(api_client): #проверка, что тело ответа в формат JSON
    response = api_client.get(path="/liveness/", verify=False)
    assert response.headers['Content-Type'] == "application/json"

def test_liveness_check_result_equals_True(api_client):   #
    response = api_client.get(path="/liveness/", verify=False)
    response_body = response.json()
    assert response_body["result"] == True

def test_api_schema_liveness(api_client): # проверка схемы страницы liveness
    response = api_client.get(path="/liveness/", verify=False)
    schema = {
        "type": "object",
        "properties": {
            "result": {"type": "boolean"},
            "version": {"type": "string"},
            "now": {"type": "string"}
        }
    }
    validate(instance=response.json(), schema=schema)