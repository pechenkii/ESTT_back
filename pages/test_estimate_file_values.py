import allure


def test_without_login_estimate_file_check_status_code_equals_403(api_client, get_id_last_estimate_file): # незалогиненный пользователь должен получать ответ 403 при получении списка значений сметы
    response = api_client.get(path="/estimate-files/" + get_id_last_estimate_file + "/values", verify=False)
    assert response.status_code == 403

def test_login_estimate_file_check_status_code_equals_200(get_login_token, api_client, get_id_last_estimate_file): # залогиненный пользователь должен получать ответ 200 при получении списка значений сметы
    response = api_client.get(path="/estimate-files/" + get_id_last_estimate_file + "/values", headers={"authorization": get_login_token}, verify=False)
    assert response.status_code == 200
    print(response.json())

def test_estimate_file_check_content_type_equals_json(api_client, get_id_last_estimate_file): # проверка, что тело ответа в формат JSON
    response = api_client.get(path="/estimate-files/" + get_id_last_estimate_file + "/values", verify=False)
    assert response.headers['Content-Type'] == "application/json"

def test_create_estimate_file_value_check_status_code_equals_201(get_login_token, api_client, get_id_first_project, get_id_last_estimate_file): # проверка создания значения сметы залогиненным пользователем, должны получить ответ 201
    data = {
        "value": 2
    }
    response = api_client.post(path="/estimate-files/" + get_id_last_estimate_file + "/values", headers={"authorization": get_login_token}, verify=False, data = data)
    assert response.status_code == 201
    print(response.json())

def test_without_login_estimate_file_value_check_status_code_equals_403(api_client, get_id_last_estimate_file, get_id_last_estimate_file_value): # незалогиненный пользователь должен получать ответ 403 при получении значения сметы
    response = api_client.get(path="/estimate-files/" + get_id_last_estimate_file + "/values/" + get_id_last_estimate_file_value, verify=False)
    assert response.status_code == 403

def test_login_estimate_file_value_check_status_code_equals_200(get_login_token, api_client, get_id_last_estimate_file, get_id_last_estimate_file_value): # залогиненный пользователь должен получать ответ 200 при получении значения сметы
    response = api_client.get(path="/estimate-files/" + get_id_last_estimate_file + "/values/" + get_id_last_estimate_file_value, headers={"authorization": get_login_token}, verify=False)
    assert response.status_code == 200
    print(response.json())

def test_full_change_estimate_file_value_check_status_code_equals_200(get_login_token, api_client, get_id_last_estimate_file, get_id_last_estimate_file_value): # проверка изменения значения сметы через put залогиненным пользователем, должны получить ответ 200
    data = {
        "value": 3
    }
    response = api_client.put(path="/estimate-files/" + get_id_last_estimate_file + "/values/" + get_id_last_estimate_file_value, headers={"authorization": get_login_token}, verify=False, data=data)
    assert response.status_code == 200
    print(response.json())

def test_change_estimate_file_value_check_status_code_equals_200(get_login_token, api_client, get_id_last_estimate_file, get_id_last_estimate_file_value): # проверка изменения значения сметы через pach залогиненным пользователем, должны получить ответ 200
    data = {
        "value": 4
    }
    response = api_client.patch(path="/estimate-files/" + get_id_last_estimate_file + "/values/" + get_id_last_estimate_file_value, headers={"authorization": get_login_token}, verify=False, data=data)
    assert response.status_code == 200
    print(response.json())

def test_delete_estimate_file_value_check_status_code_equals_204(get_login_token, api_client, get_id_last_estimate_file, get_id_last_estimate_file_value): # проверка удаления значения в смете залогиненным пользователем, должны получить ответ 204
    response = api_client.delete(path="/estimate-files/" + get_id_last_estimate_file + "/values/" + get_id_last_estimate_file_value, headers={"authorization": get_login_token}, verify=False)
    assert response.status_code == 204