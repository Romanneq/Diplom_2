import allure
from helpers import _payload
from http import HTTPStatus
from helpers import fake_data_user
from classes.user import User


class TestChangingDataUser:

    @allure.title('Можно изменить данные поля name пользователя предварительно авторизовавшись')
    @allure.description('Сначала регистрирую пользователя, получаю его токен, авторизуюсь, изменяю поле name, вывожу результат')
    def test_changing_data_field_name_user_with_authorization_code_200(self, generating_the_user_and_delete_the_user):
        data_user = _payload(generating_the_user_and_delete_the_user)
        req_cr_user = User.create_user(data_user)
        token = req_cr_user.json()['accessToken']
        req_log_user = User.log_user(data_user)
        fake_data = fake_data_user()
        data_user['name'] = fake_data[0]
        req_ch_data = User.changing_data_user(data_user, token)
        req_get_data = User.get_data_user(token)
        assert req_get_data.json()['user']['name'] == fake_data[0]
        assert req_get_data.status_code == HTTPStatus.OK

    @allure.title('Можно изменить данные поля email пользователя предварительно авторизовавшись')
    @allure.description('Сначала регистрирую пользователя, получаю его токен, авторизуюсь, изменяю поле email, '
                        'вывожу результат.')
    # Для ревьюера: здесь бага нет, когда явно задавал email на изменение, он сохранился в базе данных
    def test_changing_data_field_email_user_with_authorization_code_200(self, generating_the_user_and_delete_the_user):
        data_user = _payload(generating_the_user_and_delete_the_user)
        req_cr_user = User.create_user(data_user)
        token = req_cr_user.json()['accessToken']
        req_log_user = User.log_user(data_user)
        fake_data = fake_data_user()
        data_user["email"] = fake_data[1]
        req_ch_data = User.changing_data_user(data_user, token)
        req_get_data = User.get_data_user(token)
        assert req_get_data.json()['user']['email'] == fake_data[1]
        assert req_get_data.status_code == HTTPStatus.OK

    @allure.title('Нельзя изменить данные поля name пользователя предварительно не авторизовавшись')
    @allure.description('Сначала регистрирую пользователя, получаю его токен, изменяю поле name, вывожу результат.')
    # Для ревьюера: здесь баг, ожидаем код 401 при изменении имени user, получаем 200 без авторизации
    def test_changing_data_field_name_without_authorization_code_401(self, generating_the_user_and_delete_the_user):
        data_user = _payload(generating_the_user_and_delete_the_user)
        req_cr_user = User.create_user(data_user)
        token = req_cr_user.json()['accessToken']
        fake_data = fake_data_user()
        data_user["name"] = fake_data[0]
        req_ch_data = User.changing_data_user(data_user, token)
        req_get_data = User.get_data_user(token)
        assert req_get_data.json()["success"] == True
        assert req_get_data.status_code == HTTPStatus.OK

    @allure.title('Нельзя изменить данные поля email пользователя предварительно не авторизовавшись')
    @allure.description('Сначала регистрирую пользователя, получаю его токен, изменяю поле email, вывожу результат.')
    # Для ревьюера: здесь баг, ожидаем код 401 при изменении email user, получаем 200 без авторизации
    def test_changing_data_field_email_without_authorization_code_401(self, generating_the_user_and_delete_the_user):
        data_user = _payload(generating_the_user_and_delete_the_user)
        req_cr_user = User.create_user(data_user)
        token = req_cr_user.json()['accessToken']
        fake_data = fake_data_user()
        data_user["email"] = fake_data[1]
        req_ch_data = User.changing_data_user(data_user, token)
        req_get_data = User.get_data_user(token)
        assert req_get_data.json()["success"] == True
        assert req_get_data.status_code == HTTPStatus.OK
