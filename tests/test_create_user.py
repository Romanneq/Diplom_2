import allure
from helpers import _payload
from http import HTTPStatus
from classes.user import User


class TestCreateUser:

    @allure.title('Можно создать уникального пользователя')
    def test_create_user_code_200(self, generating_the_user_and_delete_the_user):
        data_user = _payload(generating_the_user_and_delete_the_user)
        req_cr_user = User.create_user(data_user)
        assert req_cr_user.json()['success'] == True
        assert req_cr_user.status_code == HTTPStatus.OK

    @allure.title('Нельзя создать пользователя, который уже зарегистрирован')
    def test_re_create_user_code_403(self, generating_the_user_and_delete_the_user):
        data_user = _payload(generating_the_user_and_delete_the_user)
        req_cr_user = User.create_user(data_user)
        req_re_cr_user = User.create_user(data_user)
        assert req_re_cr_user.json()['success'] == False
        assert req_re_cr_user.status_code == HTTPStatus.FORBIDDEN

    @allure.title('Нельзя создать пользователя c пустым полем name')
    def test_create_user_with_empty_field_name_code_403(self, generating_the_user_and_delete_the_user):
        data_user = _payload(generating_the_user_and_delete_the_user)
        data_user['name'] = ''
        req_cr_user = User.create_user(data_user)
        assert req_cr_user.json()['success'] == False
        assert req_cr_user.status_code == HTTPStatus.FORBIDDEN

    @allure.title('Нельзя создать пользователя c пустым полем email')
    def test_create_user_with_empty_field_email_code_403(self, generating_the_user_and_delete_the_user):
        data_user = _payload(generating_the_user_and_delete_the_user)
        data_user['email'] = ''
        req_cr_user = User.create_user(data_user)
        assert req_cr_user.json()['success'] == False
        assert req_cr_user.status_code == HTTPStatus.FORBIDDEN

    @allure.title('Нельзя создать пользователя c пустым полем password')
    def test_create_user_with_empty_field_password_code_403(self, generating_the_user_and_delete_the_user):
        data_user = _payload(generating_the_user_and_delete_the_user)
        data_user['password'] = ''
        req_cr_user = User.create_user(data_user)
        assert req_cr_user.json()['success'] == False
        assert req_cr_user.status_code == HTTPStatus.FORBIDDEN

    @allure.title('Нельзя создать пользователя c неверным полем email')
    def test_create_user_with_incorrect_field_email_code_403(self, generating_the_user_and_delete_the_user):
        data_user = _payload(generating_the_user_and_delete_the_user)
        data_user['email'] = '123'
        req_cr_user = User.create_user(data_user)
        assert req_cr_user.json()['success'] == False
        assert req_cr_user.status_code == HTTPStatus.FORBIDDEN

    @allure.title('Нельзя создать пользователя, c пустым телом запроса')
    def test_create_user_with_empty_request_body_code_403(self):
        data_user = {}
        req_cr_user = User.create_user(data_user)
        assert req_cr_user.json()['success'] == False
        assert req_cr_user.status_code == HTTPStatus.FORBIDDEN
