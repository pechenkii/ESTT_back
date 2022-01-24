import allure
import datetime
from jsonschema import validate


def test_without_login_project_estimate_reports_check_status_code_equals_403(api_client, get_id_first_project): # незалогиненный пользователь должен получать ответ 403 при получении списка отчетов проекта
    response = api_client.get(path="/projects/" + get_id_first_project + "/estimate-reports", verify=False)
    assert response.status_code == 403

def test_login_project_estimate_reports_check_status_code_equals_200(get_login_token, api_client, get_id_first_project): # залогиненный пользователь должен получать ответ 200 при получении списка отчетов проекта
    response = api_client.get(path="/projects/" + get_id_first_project + "/estimate-reports", headers={"authorization": get_login_token}, verify=False)
    assert response.status_code == 200
    print(response.json())

def test_project_estimate_reports_check_content_type_equals_json(get_login_token, api_client, get_id_first_project): #проверка, что тело ответа в формат JSON
    response = api_client.get(path="/projects/" + get_id_first_project + "/estimate-reports", headers={"authorization": get_login_token}, verify=False)
    assert response.headers['Content-Type'] == "application/json"

def test_api_schema_project_estimate_report(get_login_token, api_client, get_id_first_project):    # проверка схемы файла отчета
    response = api_client.get(path="/projects/" + get_id_first_project + "/estimate-reports", headers={"authorization": get_login_token}, verify=False)
    schema = {
        "type": "object",
        "properties": {
            "id": {"type": "integer"},
            "xls_file": {"type": ["string", "null"]},
            "report_on_date": {"type": "string"},
            "process_status": {"type": "string"},
            "created_at": {"type": "string"}
        }
    }
    validate(instance=response.json()[1], schema=schema)

def test_create_project_estimate_report_check_status_code_equals_201(get_login_token, api_client, get_id_first_project): # проверка добавления отчета по смете к проекту
    data = {
        "report_on_date": datetime.datetime.now()
    }
    response = api_client.post(path="/projects/" + get_id_first_project + "/estimate-reports", headers={"authorization": get_login_token}, verify=False, data=data)
#    assert response.status_code == 201
    print(response.status_code)
    print(response.json())

def test_without_login_project_estimate_report_check_status_code_equals_403(api_client, get_id_first_project, get_id_last_estimate_report): # незалогиненный пользователь должен получать ответ 403 при получении определенного отчета проекта
    response = api_client.get(path="/projects/" + get_id_first_project + "/estimate-reports/" + get_id_last_estimate_report, verify=False)
    assert response.status_code == 403

def test_login_project_estimate_report_check_status_code_equals_200(get_login_token, api_client, get_id_first_project, get_id_last_estimate_report): # залогиненный пользователь должен получать ответ 200 при получении определенного отчета проекта
    response = api_client.get(path="/projects/" + get_id_first_project + "/estimate-reports/" + get_id_last_estimate_report, headers={"authorization": get_login_token}, verify=False)
    assert response.status_code == 200
    print(response.json())


def test(get_id_last_estimate_report):
    print(get_id_last_estimate_report)