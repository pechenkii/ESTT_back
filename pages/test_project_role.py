import allure

def test_without_login_project_roles_check_status_code_equals_403(api_client, get_id_first_project): # незалогиненный пользователь должен получать ответ 401 при получении списка ролей у проекта
    response = api_client.get(path="/projects/" + get_id_first_project + "/role-assignments/", verify=False)
    assert response.status_code == 403

def test_login_project_roles_check_status_code_equals_200(get_login_token, api_client, get_id_first_project):  # залогиненный пользователь должен получать ответ 200 при получении списка ролей у проекта
    response = api_client.get(path="/projects/" + get_id_first_project + "/role-assignments/", headers={"authorization": get_login_token}, verify=False)
    assert response.status_code == 200
    print(response.json())

def test_create_project_role_check_status_code_equals_201(get_login_token, api_client, get_id_first_project): #проверка создания роли в проекте залогиненным пользователем, должны получить ответ 201
    data = {
        "user": 2,
        "role": 1,
        "project": get_id_first_project
    }
    response = api_client.post(path="/projects/" + get_id_first_project + "/role-assignments/", headers={"authorization": get_login_token}, verify=False, data = data)
    assert response.status_code == 201
#    print(response.json())

def test_without_login_project_role_check_status_code_equals_403(get_id_last_role, api_client, get_id_first_project): # незалогиненный пользователь должен получать ответ 403 при получении определенной роли в проекте
    response = api_client.get(path="/projects/" + get_id_first_project + "/role-assignments/" + get_id_last_role, verify=False, params={'is_active': True, 'name': 'Рабочие'})
    assert response.status_code == 403

def test_login_project_role_check_status_code_equals_200(get_login_token,get_id_last_role, api_client, get_id_first_project): # залогиненный пользователь должен получать ответ 200 при получении определенной роли в проекте
    response = api_client.get(path="/projects/" + get_id_first_project + "/role-assignments/" + get_id_last_role, headers={"authorization": get_login_token}, verify=False, params={'is_active': True, 'name': 'Рабочие'})
    assert response.status_code == 200

def test_change_project_role_check_status_code_equals_200(get_login_token,get_id_last_role, api_client, get_id_first_project): #проверка изменения роли в проекте залогиненным пользователем, должны получить ответ 200
    data = {
        "user": 2,
        "role": 4,
        "project": get_id_first_project
    }
    response = api_client.put(path="/projects/" + get_id_first_project + "/role-assignments/" + get_id_last_role, headers={"authorization": get_login_token}, verify=False, data = data)
    assert response.status_code == 200
    print(response.json())

def test_delete_project_role_check_status_code_equals_204(get_login_token,get_id_last_role, api_client, get_id_first_project): #проверка  удаления роли в проекте залогиненным пользователем, должны получить ответ 204
    response = api_client.delete(path="/projects/" + get_id_first_project + "/role-assignments/" + get_id_last_role, headers={"authorization": get_login_token}, verify=False)
    assert response.status_code == 204
#    print(response.json())

