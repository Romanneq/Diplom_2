import allure
import requests
from data import URL
from data import Endpoint


class TestCreateUser:

    @allure.title('Можно создать уникального пользователя')
    def test_create_user_code_200(self, generating_the_cour_and_delete_the_cour):
        payload = {"name": generating_the_cour_and_delete_the_cour[0],
                   "email": generating_the_cour_and_delete_the_cour[1],
                   "password": generating_the_cour_and_delete_the_cour[2]}
        response = requests.post(f'{URL}{Endpoint.create_user}', data=payload)
        assert response.json()['success'] == True
        assert response.status_code == 200

    @allure.title('Нельзя создать пользователя, который уже зарегистрирован')
    def test_re_create_user_code_403(self, generating_the_cour_and_delete_the_cour):
        payload = {"name": generating_the_cour_and_delete_the_cour[0],
                   "email": generating_the_cour_and_delete_the_cour[1],
                   "password": generating_the_cour_and_delete_the_cour[2]}
        requests.post(f'{URL}{Endpoint.create_user}', data=payload)
        response_re = requests.post(f'{URL}{Endpoint.create_user}', data=payload)
        assert response_re.json()['success'] == False
        assert response_re.status_code == 403

    @allure.title('Нельзя создать пользователя c пустым полем name')
    def test_create_user_with_empty_field_name_code_403(self, generating_the_cour_and_delete_the_cour):
        payload = {"name": '',
                   "email": generating_the_cour_and_delete_the_cour[1],
                   "password": generating_the_cour_and_delete_the_cour[2]}
        response = requests.post(f'{URL}{Endpoint.create_user}', data=payload)
        assert response.json()['success'] == False
        assert response.status_code == 403

    @allure.title('Нельзя создать пользователя c пустым полем email')
    def test_create_user_with_empty_field_email_code_403(self, generating_the_cour_and_delete_the_cour):
        payload = {"name": generating_the_cour_and_delete_the_cour[0],
                   "email": '',
                   "password": generating_the_cour_and_delete_the_cour[2]}
        response = requests.post(f'{URL}{Endpoint.create_user}', data=payload)
        assert response.json()['success'] == False
        assert response.status_code == 403

    @allure.title('Нельзя создать пользователя c пустым полем password')
    def test_create_user_with_empty_field_password_code_403(self, generating_the_cour_and_delete_the_cour):
        payload = {"name": generating_the_cour_and_delete_the_cour[0],
                   "email": generating_the_cour_and_delete_the_cour[1],
                   "password": ''}
        response = requests.post(f'{URL}{Endpoint.create_user}', data=payload)
        assert response.json()['success'] == False
        assert response.status_code == 403

    @allure.title('Нельзя создать пользователя c неверным полем email')
    def test_create_user_with_incorrect_field_email_code_403(self, generating_the_cour_and_delete_the_cour):
        payload = {"name": generating_the_cour_and_delete_the_cour[0],
                   "email": '123',
                   "password": generating_the_cour_and_delete_the_cour[2]}
        response = requests.post(f'{URL}{Endpoint.create_user}', data=payload)
        assert response.json()['success'] == False
        assert response.status_code == 403

    @allure.title('Нельзя создать пользователя, c пустым телом запроса')
    def test_create_user_with_empty_request_body_code_403(self):
        payload = {}
        response = requests.post(f'{URL}{Endpoint.create_user}', data=payload)
        assert response.json()['success'] == False
        assert response.status_code == 403