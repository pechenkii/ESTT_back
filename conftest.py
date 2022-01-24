import requests
import pytest


class APIClient: # описание API - клиента для отправки запросов на базовый URL
    def __init__(self, base_address):
        self.base_address = base_address

    def get(self, path="/", params=None, headers=None, verify=False): # инициализация GET - запроса на получение данных
        url = self.base_address + path
        print("GET request to {}".format(url))
        return requests.get(url=url, params=params, headers=headers, verify=verify)

    def post(self, path="/", params=None, data=None, headers=None, verify=False, files=None): # инициализация POST - запроса на внесение данных
        url = self.base_address + path
        print("POST request to {}".format(url))
        return requests.post(url=url, params=params, data=data, headers=headers, verify=verify, files=files)

    def put(self, path="/", params=None, data=None, headers=None, verify=False, files=None): # инициализация PUT - запроса на изменение данных
        url = self.base_address + path
        print("PUT request to {}".format(url))
        return requests.put(url=url, params=params, data=data, headers=headers, verify=verify, files=files)

    def patch(self, path="/", params=None, data=None, headers=None, verify=False, files=None): # инициализация PATCH - запроса на изменение части данных
        url = self.base_address + path
        print("PATCH request to {}".format(url))
        return requests.patch(url=url, params=params, data=data, headers=headers, verify=verify, files=files)

    def delete(self, path="/", params=None, headers=None, verify=False): # инициализация DELETE - запроса на удаление данных
        url = self.base_address + path
        print("DELETE request to {}".format(url))
        return requests.delete(url=url, params=params, headers=headers, verify=verify)

@pytest.fixture()
def api_client(): # описание объекта API - клиента c объявленным базовым URL-ом
    return APIClient(base_address="https://estate.xcloud-dev.x5.ru/api")

@pytest.fixture()
def get_login_token(): #получение токена для авторизации от keycloak
    response = requests.post("https://estate-keyc-124.x5.ru/auth/realms/x5ad/protocol/openid-connect/token",
                             verify=False, data=[('username', 'evg.myasnikov'), ('password', 'Repbyju666'),
                                                 ('grant_type', 'password'), ('scope', 'openid'),
                                                 ('client_id', 'account'),
                                                 ('client_secret', 'dd06da58-fc08-4eb5-a5c4-31fb918193f4'), ])
    response_body = response.json()
    token = "Bearer " + response_body["access_token"]
    return token

@pytest.fixture()
def get_id_first_project(get_login_token, api_client): # получение id  первого проекта, в котором будем проводить тесты
    response = api_client.get(path="/projects/", headers={'authorization': get_login_token},
                            verify=False)
    a=[]
    for i in range(len(response.json())):
        a.append(response.json()[i]["id"])
    id=str(min(a))
    return id

@pytest.fixture()
def get_id_last_risk(get_login_token, api_client): # получение id последнего риска
    response = api_client.get(path="/risks/", headers={'authorization': get_login_token},
                            verify=False)
    a=[]
    for i in range(len(response.json())):
        a.append(response.json()[i]["id"])
    id=str(max(a))
    return id

@pytest.fixture()
def get_id_last_role(get_login_token, api_client, get_id_first_project): # получение id последней роли в проекте
    response = api_client.get(path="/projects/" + get_id_first_project + "/role-assignments/", headers={'authorization': get_login_token},
                            verify=False)
    a=[]
    for i in range(len(response.json())):
        a.append(response.json()[i]["id"])
    id=str(max(a))
    return id

@pytest.fixture()
def get_id_last_foto(get_login_token, api_client, get_id_first_project): # получение id последнего фото
    response = api_client.get(path="/projects/" + get_id_first_project + "/photos/", headers={'authorization': get_login_token},
                            verify=False)
    a=[]
    for i in range(len(response.json())):
        a.append(response.json()[i]["id"])
    id=str(max(a))
    return id

@pytest.fixture()
def get_id_last_estimate_file(get_login_token, api_client, get_id_first_project): # получение id последнего файла сметы у проекта
    response = api_client.get(path="/projects/" + get_id_first_project + "/estimate-files", headers={'authorization': get_login_token},
                            verify=False)
    a=[]
    for i in range(len(response.json())):
        a.append(response.json()[i]["id"])
    id=str(max(a))
    return id

@pytest.fixture()
def get_id_last_estimate_file_row(get_login_token, api_client, get_id_first_project, get_id_last_estimate_file): # получение id последней строки сметы у проекта
    response = api_client.get(path="/projects/" + get_id_first_project + "/estimate-files/" + get_id_last_estimate_file + "/rows", headers={'authorization': get_login_token},
                            verify=False)
    a=[]
    for i in range(len(response.json())):
        a.append(response.json()[i]["id"])
    id=str(max(a))
    return id

@pytest.fixture()
def get_id_last_estimate_file_value(get_login_token, api_client, get_id_first_project, get_id_last_estimate_file, get_id_last_estimate_file_row): # получение id последнего ... файла сметы у проекта
    response = api_client.get(path="/projects/" + get_id_first_project + "/estimate-files/" + get_id_last_estimate_file + "/rows/" + get_id_last_estimate_file_row + "/values", headers={'authorization': get_login_token},
                            verify=False)
    a=[]
    for i in range(len(response.json())):
        a.append(response.json()[i]["id"])
    id=str(max(a))
    return id

@pytest.fixture()
def get_id_last_estimate_report(get_login_token, api_client, get_id_first_project): # получение id последнего отчета сметы у проекта
    response = api_client.get(path="/projects/" + get_id_first_project + "/estimate-reports", headers={'authorization': get_login_token},
                            verify=False)
    a=[]
    for i in range(len(response.json())):
        a.append(response.json()[i]["id"])
    id=str(max(a))
    return id
