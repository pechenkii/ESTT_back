import allure
import datetime

def test_without_login_projects_estimate_row_today_value_check_status_code_equals_403(get_login_token, api_client, get_id_first_project, get_id_last_estimate_file,get_id_last_estimate_file_row): # незалогиненный пользователь должен получать ответ 403 при получении значения на сегодня строки сметы проекта
    response = api_client.get(path="/projects/" + get_id_first_project + "/estimate-files/" + get_id_last_estimate_file + "/rows/" + get_id_last_estimate_file_row + "/today-values", verify=False)
    assert response.status_code == 403

def test_login_projects_estimate_row_today_value_check_status_code_equals_200(get_login_token, api_client, get_id_first_project, get_id_last_estimate_file,get_id_last_estimate_file_row): # залогиненный пользователь должен получать ответ 200 при получении значения на сегодня строки сметы проекта
    response = api_client.get(path="/projects/" + get_id_first_project + "/estimate-files/" + get_id_last_estimate_file + "/rows/" + get_id_last_estimate_file_row  + "/today-values", headers={"authorization": get_login_token}, verify=False)
    assert response.status_code == 200
    print(response.json())

def test_without_login_project_estimate_file_row_values_check_status_code_equals_403(api_client, get_id_last_estimate_file, get_id_first_project, get_id_last_estimate_file_row): # незалогиненный пользователь должен получать ответ 403 при получении списка значений сметы
    response = api_client.get(path="/projects/" + get_id_first_project + "/estimate-files/" + get_id_last_estimate_file + "/rows/" + get_id_last_estimate_file_row + "/values", verify=False)
    assert response.status_code == 403

def test_login_project_estimate_file_row_values_check_status_code_equals_200(get_login_token, api_client, get_id_last_estimate_file, get_id_first_project, get_id_last_estimate_file_row): # залогиненный пользователь должен получать ответ 200 при получении списка значений сметы
    response = api_client.get(path="/projects/" + get_id_first_project + "/estimate-files/" + get_id_last_estimate_file + "/rows/" + get_id_last_estimate_file_row + "/values", headers={"authorization": get_login_token}, verify=False)
    assert response.status_code == 200
    print(response.json())

def test_project_estimate_file_row_values_check_content_type_equals_json(get_login_token, api_client, get_id_last_estimate_file, get_id_first_project, get_id_last_estimate_file_row): # проверка, что тело ответа в формат JSON
    response = api_client.get(path="/projects/" + get_id_first_project + "/estimate-files/" + get_id_last_estimate_file + "/rows/" + get_id_last_estimate_file_row + "/values", headers={"authorization": get_login_token}, verify=False)
    assert response.headers['Content-Type'] == "application/json"

def test_create_project_estimate_file_row_value_check_status_code_equals_201(get_login_token, api_client, get_id_first_project, get_id_last_estimate_file, get_id_last_estimate_file_row): # проверка создания значения сметы залогиненным пользователем, должны получить ответ 201
    data = {
        "value": 2,
        "provided_at": datetime.date.today()
    }
    response = api_client.post(path="/projects/" + get_id_first_project + "/estimate-files/" + get_id_last_estimate_file + "/rows/" + get_id_last_estimate_file_row + "/values", headers={"authorization": get_login_token}, verify=False, data=data)
    assert response.status_code == 201
    print(response.json())

def test_second_create_project_estimate_file_row_value_check_status_code_equals_400(get_login_token, api_client, get_id_first_project, get_id_last_estimate_file, get_id_last_estimate_file_row): # проверка повторного создания значения сметы(с теми же данными) залогиненным пользователем, должны получить ответ 400
    data = {
        "value": 2,
        "provided_at": datetime.date.today()
    }
    response = api_client.post(path="/projects/" + get_id_first_project + "/estimate-files/" + get_id_last_estimate_file + "/rows/" + get_id_last_estimate_file_row + "/values", headers={"authorization": get_login_token}, verify=False, data=data)
    assert response.status_code == 400

def test_without_login_estimate_file_value_check_status_code_equals_403(api_client, get_id_last_estimate_file, get_id_first_project, get_id_last_estimate_file_row, get_id_last_estimate_file_value): # незалогиненный пользователь должен получать ответ 403 при получении определенного значения сметы
    response = api_client.get(path="/projects/" + get_id_first_project + "/estimate-files/" + get_id_last_estimate_file + "/rows/" + get_id_last_estimate_file_row + "/values/" + get_id_last_estimate_file_value, verify=False)
    assert response.status_code == 403

def test(get_id_first_project, get_id_last_estimate_file, get_id_last_estimate_file_row, get_id_last_estimate_file_value):
    print(get_id_first_project, get_id_last_estimate_file, get_id_last_estimate_file_row, get_id_last_estimate_file_value)

def test_login_project_estimate_file_row_value_check_status_code_equals_200(get_login_token, api_client, get_id_last_estimate_file, get_id_first_project, get_id_last_estimate_file_row, get_id_last_estimate_file_value): # залогиненный пользователь должен получать ответ 200 при получении определенного значения сметы
    response = api_client.get(path="/projects/" + get_id_first_project + "/estimate-files/" + get_id_last_estimate_file + "/rows/" + get_id_last_estimate_file_row + "/values/" + get_id_last_estimate_file_value, headers={"authorization": get_login_token}, verify=False)
    assert response.status_code == 200
    print(response.json())

def test_change_project_estimate_file_row_value_check_status_code_equals_200(get_login_token, api_client, get_id_first_project, get_id_last_estimate_file, get_id_last_estimate_file_row, get_id_last_estimate_file_value): # проверка изменения определенного значения сметы через pach залогиненным пользователем, должны получить ответ 200
    data = {
        "value": 1
    }
    response = api_client.patch(path="/projects/" + get_id_first_project + "/estimate-files/" + get_id_last_estimate_file + "/rows/" + get_id_last_estimate_file_row + "/values/" + get_id_last_estimate_file_value, headers={"authorization": get_login_token}, verify=False, data=data)
    assert response.status_code == 200
    print(response.json())

def test_delete_estimate_file_value_check_status_code_equals_204(get_login_token, api_client, get_id_first_project, get_id_last_estimate_file, get_id_last_estimate_file_row, get_id_last_estimate_file_value): # проверка удаления значения в смете залогиненным пользователем, должны получить ответ 204
    response = api_client.delete(path="/projects/" + get_id_first_project + "/estimate-files/" + get_id_last_estimate_file + "/rows/" + get_id_last_estimate_file_row + "/values/" + get_id_last_estimate_file_value, headers={"authorization": get_login_token}, verify=False)
    assert response.status_code == 204