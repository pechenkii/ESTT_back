import allure

def test_without_login_project_risks_check_status_code_equals_403(api_client, get_id_first_project):    # незалогиненный пользователь должен получать ответ 403 при получении списка рисков в проекте
    response = api_client.get(path="/projects/" + get_id_first_project + "/risks/", verify=False)
    assert response.status_code == 403

def test_login_project_risk_check_status_code_equals_200(get_login_token, api_client, get_id_first_project): # залогиненный пользователь должен получать ответ 200 при получении списка рисков в проекте
    response = api_client.get(path="/projects/" + get_id_first_project + "/risks/", headers={"authorization": get_login_token}, verify=False)
    assert response.status_code == 200

