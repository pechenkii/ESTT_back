import allure

def test_without_login_get_me_check_status_code_equals_403(api_client): # незалогиненный пользователь должен получать ответ 403 при получении своего имени
    response = api_client.get(path="/get-me/", verify=False)
    assert response.status_code == 403

def test_login_get_me_check_status_code_equals_200(get_login_token, api_client): # залогиненный пользователь должен получать ответ 200 при получении своего имени
    response = api_client.get(path="/get-me/", headers={"authorization": get_login_token}, verify=False)
    assert response.status_code == 200
    print(response.json())

def test_get_me_check_content_type_equals_json(get_login_token, api_client): #проверка, что тело ответа в формат JSON
    response = api_client.get(path="/get-me/", verify=False)
    assert response.headers['Content-Type'] == "application/json"