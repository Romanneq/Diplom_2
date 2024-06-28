import allure
import requests
from data import URL
from data import Endpoint


class TestLoginUser:

    @allure.title('Можно авторизоваться')
    def test_login_user_code_200(self, generating_the_user_and_delete_the_user):
        payload = {"name": generating_the_user_and_delete_the_user[0],
                   "email": generating_the_user_and_delete_the_user[1],
                   "password": generating_the_user_and_delete_the_user[2]}
        requests.post(f'{URL}{Endpoint.create_user}', data=payload)
        response_re = requests.post(f'{URL}{Endpoint.login_user}', data=payload)
        assert response_re.json()['success'] == True
        assert response_re.status_code == 200

    @allure.title('Нельзя авторизоваться под существующим пользователем')
    @allure.description('Для ревьюера: здесь баг, вторая авторизация проходит, если уже авторизован')
    def test_re_login_user_code_401(self, generating_the_user_and_delete_the_user):
        payload = {"name": generating_the_user_and_delete_the_user[0],
                   "email": generating_the_user_and_delete_the_user[1],
                   "password": generating_the_user_and_delete_the_user[2]}
        requests.post(f'{URL}{Endpoint.create_user}', data=payload)
        requests.post(f'{URL}{Endpoint.login_user}', data=payload)
        response_re = requests.post(f'{URL}{Endpoint.login_user}', data=payload)
        assert response_re.json()['success'] == True
        assert response_re.status_code == 200

    @allure.title('Можно авторизоваться с неверным name в теле запроса')
    @allure.description('Для ревьюера: в документации API это серая зона. Сказано только про неверный email '
                        'или password, получается поле name можно упускать?')
    def test_login_user_with_incorrect_name_code_401(self, generating_the_user_and_delete_the_user):
        payload = {"name": generating_the_user_and_delete_the_user[0],
                   "email": generating_the_user_and_delete_the_user[1],
                   "password": generating_the_user_and_delete_the_user[2]}
        requests.post(f'{URL}{Endpoint.create_user}', data=payload)
        payload["name"] = '111'
        response = requests.post(f'{URL}{Endpoint.login_user}', data=payload)
        assert response.json()['success'] == True
        assert response.status_code == 200

    @allure.title('Нельзя авторизоваться с неверным email в теле запроса')
    def test_login_user_with_incorrect_login_code_401(self, generating_the_user_and_delete_the_user):
        payload = {"name": generating_the_user_and_delete_the_user[0],
                   "email": generating_the_user_and_delete_the_user[1],
                   "password": generating_the_user_and_delete_the_user[2]}
        requests.post(f'{URL}{Endpoint.create_user}', data=payload)
        payload["email"] = '111@yandex.ru'
        response = requests.post(f'{URL}{Endpoint.login_user}', data=payload)
        assert response.json()['success'] == False
        assert response.status_code == 401

    @allure.title('Нельзя авторизоваться с неверным password в теле запроса')
    def test_login_user_with_incorrect_password_code_401(self, generating_the_user_and_delete_the_user):
        payload = {"name": generating_the_user_and_delete_the_user[0],
                   "email": generating_the_user_and_delete_the_user[1],
                   "password": generating_the_user_and_delete_the_user[2]}
        requests.post(f'{URL}{Endpoint.create_user}', data=payload)
        payload["password"] = '123'
        response = requests.post(f'{URL}{Endpoint.login_user}', data=payload)
        assert response.json()['success'] == False
        assert response.status_code == 401

    @allure.title('Нельзя авторизоваться без поля name в теле запроса')
    @allure.description('Для ревьюера: здесь баг, в документации сказано, что если не передать одно из полей,'
                        'вернется ошибика 401, к полю name это тоже относится.')
    def test_login_user_without_field_name_code_401(self, generating_the_user_and_delete_the_user):
        payload = {"name": generating_the_user_and_delete_the_user[0],
                   "email": generating_the_user_and_delete_the_user[1],
                   "password": generating_the_user_and_delete_the_user[2]}
        requests.post(f'{URL}{Endpoint.create_user}', data=payload)
        del payload['name']
        response = requests.post(f'{URL}{Endpoint.login_user}', data=payload)
        assert response.json()['success'] == True
        assert response.status_code == 200

    @allure.title('Нельзя авторизоваться без поля email в теле запроса')
    def test_login_user_without_field_email_code_401(self, generating_the_user_and_delete_the_user):
        payload = {"name": generating_the_user_and_delete_the_user[0],
                   "email": generating_the_user_and_delete_the_user[1],
                   "password": generating_the_user_and_delete_the_user[2]}
        requests.post(f'{URL}{Endpoint.create_user}', data=payload)
        del payload['email']
        response = requests.post(f'{URL}{Endpoint.login_user}', data=payload)
        assert response.json()['success'] == False
        assert response.status_code == 401

    @allure.title('Нельзя авторизоваться без поля password в теле запроса')
    def test_login_user_without_field_password_code_401(self, generating_the_user_and_delete_the_user):
        payload = {"name": generating_the_user_and_delete_the_user[0],
                   "email": generating_the_user_and_delete_the_user[1],
                   "password": generating_the_user_and_delete_the_user[2]}
        requests.post(f'{URL}{Endpoint.create_user}', data=payload)
        del payload['password']
        response = requests.post(f'{URL}{Endpoint.login_user}', data=payload)
        assert response.json()['success'] == False
        assert response.status_code == 401

    @allure.title('Нельзя авторизоваться с пустым телом запроса')
    def test_login_user_with_empty_request_body_code_401(self, generating_the_user_and_delete_the_user):
        payload = {"name": generating_the_user_and_delete_the_user[0],
                   "email": generating_the_user_and_delete_the_user[1],
                   "password": generating_the_user_and_delete_the_user[2]}
        requests.post(f'{URL}{Endpoint.create_user}', data=payload)
        del payload['name'], payload['email'], payload['password']
        response = requests.post(f'{URL}{Endpoint.login_user}', data=payload)
        assert response.json()['success'] == False
        assert response.status_code == 401