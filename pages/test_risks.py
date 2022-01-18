import allure
from jsonschema import validate

def test_without_login_risks_check_status_code_equals_403(api_client):    # незалогиненный пользователь должен получать ответ 403 при получении списка рисков
    response = api_client.get(path="/risks/", verify=False)
    assert response.status_code == 403

def test_login_risks_check_status_code_equals_200(get_login_token, api_client): # залогиненный пользователь должен получать ответ 200 при получении списка рисков
    response = api_client.get(path="/risks/", headers={"authorization": get_login_token}, verify=False)
    assert response.status_code == 200
    print(response.json())


def test_login_risk_check_status_code_equals_200(get_login_token, api_client, get_id_last_risk): # залогиненный пользователь должен получать ответ 200 при получении определенного риска
    response = api_client.get(path="/risks/" + get_id_last_risk, headers={"authorization": get_login_token}, verify=False)
    assert response.status_code == 200
    print(response.json())

def test_risks_check_content_type_equals_json(get_login_token, api_client): #проверка, что тело ответа в формат JSON
    response = api_client.get(path="/risks/", headers={"authorization": get_login_token}, verify=False)
    assert response.headers['Content-Type'] == "application/json"

def test_api_schema_risks_id(get_login_token, api_client):    # проверка схемы страницы 1 риска(ждем появления первого риска)
    response = api_client.get(path="/risks/", headers={"authorization": get_login_token}, verify=False)
    schema = {
        "type": "object",
        "properties": {
            "id": {"type": "integer"},
            "discription": {"type": "string"},
            "project": {"type": "integer"},
            "owner": {"type": "string"}
        }
    }
    validate(instance=response.json()[1], schema=schema)

def test_create_risk_check_status_code_equals_201(get_login_token,api_client, get_id_first_project): #проверка создания риска залогиненным пользователем, должны получить ответ 201
    data = {
        "description": "1234",
        "project": get_id_first_project
    }
    response = api_client.post(path="/risks/", headers={"authorization": get_login_token}, data=data, verify=False)
    assert response.status_code == 201
    print(response.json())

def test_create_blank_risk_check_status_code_equals_400(get_login_token,api_client, get_id_first_project): #проверка создания пустого риска залогиненным пользователем, должны получить ответ 400
    data = {
        "description": "",
        "project": get_id_first_project
    }
    response = api_client.post(path="/risks/", headers={"authorization": get_login_token}, data=data, verify=False)
    assert response.status_code == 400

def test_full_change_risk_check_status_code_equals_200(get_login_token, get_id_last_risk, api_client): #проверка изменения риска залогиненным пользователем, должны получить ответ 200
    data = {
        "description": "Новый текст тестового риска"
    }
    response = api_client.put(path="/risks/" + get_id_last_risk, headers={"authorization": get_login_token}, verify=False, data = data)
    assert response.status_code == 200

def test_risk_check_description_new_text(get_login_token, get_id_last_risk, api_client): #проверка того, что изменения применились
    response = api_client.get(path="/risks/" + get_id_last_risk, headers={"authorization": get_login_token}, verify=False)
    response_body = response.json()
    assert response_body["description"] == "Новый текст тестового риска"

'''def test_change_risk_check_status_code_equals_200(get_login_token, get_id_last_risk, api_client): #проверка изменения риска залогиненным пользователем, должны получить ответ 200
    response = api_client.patch("https://estate.xcloud-dev.x5.ru/api/risks/" + get_id_last_risk, headers={"authorization": get_login_token}, verify=False)
    assert response.status_code == 200'''

'''def test_print_id(get_login_token, get_id_last_risk, api_client):
    response = api_client.patch(path="/risks/" + get_id_last_risk,
                              headers={"authorization": get_login_token}, verify=False)
    print(get_id_last_risk)'''

def test_change_risk_check_status_code_equals_200(get_login_token, get_id_last_risk, api_client): #проверка изменения риска залогиненным пользователем, должны получить ответ 200
    data = {
        "description": "Пропатченный текст тестового риска"
    }
    response = api_client.patch(path="/risks/" + get_id_last_risk, headers={"authorization": get_login_token}, verify=False, data = data)
    assert response.status_code == 200
    print(response.json())




