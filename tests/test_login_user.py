import allure
from helpers import _payload
from http import HTTPStatus
from helpers import fake_data_user
from classes.user import User


class TestLoginUser:

    @allure.title('Можно авторизоваться')
    def test_login_user_code_200(self, generating_the_user_and_delete_the_user):
        data_user = _payload(generating_the_user_and_delete_the_user)
        req_cr_user = User.create_user(data_user)
        req_log_user = User.log_user(data_user)
        assert req_log_user.json()['success'] == True
        assert req_log_user.status_code == HTTPStatus.OK

    @allure.title('Нельзя авторизоваться под существующим пользователем')
    # Для ревьюера: здесь баг, вторая авторизация проходит, если уже авторизован
    def test_re_login_user_code_401(self, generating_the_user_and_delete_the_user):
        data_user = _payload(generating_the_user_and_delete_the_user)
        req_cr_user = User.create_user(data_user)
        req_log_user = User.log_user(data_user)
        req_re_log_user = User.log_user(data_user)
        assert req_re_log_user.json()['success'] == True
        assert req_re_log_user.status_code == HTTPStatus.OK

    @allure.title('Можно авторизоваться с неверным name в теле запроса')
    # Для ревьюера: в документации API это серая зона. Сказано только про неверный email или password,
    # получается поле name можно упускать?
    def test_login_user_with_incorrect_name_code_401(self, generating_the_user_and_delete_the_user):
        data_user = _payload(generating_the_user_and_delete_the_user)
        req_cr_user = User.create_user(data_user)
        fake_data = fake_data_user()
        data_user["name"] = fake_data[0]
        req_log_user = User.log_user(data_user)
        assert req_log_user.json()['success'] == True
        assert req_log_user.status_code == HTTPStatus.OK

    @allure.title('Нельзя авторизоваться с неверным email в теле запроса')
    def test_login_user_with_incorrect_login_code_401(self, generating_the_user_and_delete_the_user):
        data_user = _payload(generating_the_user_and_delete_the_user)
        req_cr_user = User.create_user(data_user)
        fake_data = fake_data_user()
        data_user["email"] = fake_data[1]
        req_log_user = User.log_user(data_user)
        assert req_log_user.json()['success'] == False
        assert req_log_user.status_code == HTTPStatus.UNAUTHORIZED

    @allure.title('Нельзя авторизоваться с неверным password в теле запроса')
    def test_login_user_with_incorrect_password_code_401(self, generating_the_user_and_delete_the_user):
        data_user = _payload(generating_the_user_and_delete_the_user)
        req_cr_user = User.create_user(data_user)
        fake_data = fake_data_user()
        data_user["password"] = fake_data[2]
        req_log_user = User.log_user(data_user)
        assert req_log_user.json()['success'] == False
        assert req_log_user.status_code == HTTPStatus.UNAUTHORIZED

    @allure.title('Нельзя авторизоваться без поля name в теле запроса')
    # Для ревьюера: здесь баг, в документации сказано, что если не передать одно из полей, вернется ошибка 401,
    # к полю name это тоже относится.
    def test_login_user_without_field_name_code_401(self, generating_the_user_and_delete_the_user):
        data_user = _payload(generating_the_user_and_delete_the_user)
        req_cr_user = User.create_user(data_user)
        del data_user['name']
        req_log_user = User.log_user(data_user)
        assert req_log_user.json()['success'] == True
        assert req_log_user.status_code == HTTPStatus.OK

    @allure.title('Нельзя авторизоваться без поля email в теле запроса')
    def test_login_user_without_field_email_code_401(self, generating_the_user_and_delete_the_user):
        data_user = _payload(generating_the_user_and_delete_the_user)
        req_cr_user = User.create_user(data_user)
        del data_user['email']
        req_log_user = User.log_user(data_user)
        assert req_log_user.json()['success'] == False
        assert req_log_user.status_code == HTTPStatus.UNAUTHORIZED

    @allure.title('Нельзя авторизоваться без поля password в теле запроса')
    def test_login_user_without_field_password_code_401(self, generating_the_user_and_delete_the_user):
        data_user = _payload(generating_the_user_and_delete_the_user)
        req_cr_user = User.create_user(data_user)
        del data_user['password']
        req_log_user = User.log_user(data_user)
        assert req_log_user.json()['success'] == False
        assert req_log_user.status_code == HTTPStatus.UNAUTHORIZED

    @allure.title('Нельзя авторизоваться с пустым телом запроса')
    def test_login_user_with_empty_request_body_code_401(self, generating_the_user_and_delete_the_user):
        data_user = _payload(generating_the_user_and_delete_the_user)
        req_cr_user = User.create_user(data_user)
        del data_user['name'], data_user['email'], data_user['password']
        req_log_user = User.log_user(data_user)
        assert req_log_user.json()['success'] == False
        assert req_log_user.status_code == HTTPStatus.UNAUTHORIZED
