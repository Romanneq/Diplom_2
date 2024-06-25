import allure
import requests
from data import URL
from data import Endpoint


class TestChangingDataUser:

    @allure.title('Можно изменить данные поля name пользователя предварительно авторизовавшись')
    @allure.description('Сначала регистрирую пользователя, получаю его токен, авторизуюсь, изменяю поле name, вывожу результат')
    def test_changing_data_field_name_user_with_authorization_code_200(self, generating_the_cour_and_delete_the_cour):
        payload = {"name": generating_the_cour_and_delete_the_cour[0],
                   "email": generating_the_cour_and_delete_the_cour[1],
                   "password": generating_the_cour_and_delete_the_cour[2]}
        res_cr_user = requests.post(f'{URL}{Endpoint.create_user}', data=payload)
        token = res_cr_user.json()['accessToken']
        requests.post(f'{URL}{Endpoint.login_user}', data=payload)
        payload["name"] = '111'
        response_ch_data = requests.patch(f'{URL}{Endpoint.del_and_change_user}', data=payload,
                                          headers={'Authorization':token})
        response_get_data = requests.get(f'{URL}{Endpoint.del_and_change_user}', headers={'Authorization': token})
        assert response_get_data.json()['user']['name'] == "111"
        assert response_get_data.status_code == 200

    @allure.title('Можно изменить данные поля email пользователя предварительно авторизовавшись')
    @allure.description('Сначала регистрирую пользователя, получаю его токен, авторизуюсь, изменяю поле email, '
                        'вывожу результат. Для ревьюера: email не изменяется, здесь баг.')
    def test_changing_data_field_email_user_with_authorization_code_200(self, generating_the_cour_and_delete_the_cour):
        payload = {"name": generating_the_cour_and_delete_the_cour[0],
                   "email": generating_the_cour_and_delete_the_cour[1],
                   "password": generating_the_cour_and_delete_the_cour[2]}
        res_cr_user = requests.post(f'{URL}{Endpoint.create_user}', data=payload)
        token = res_cr_user.json()['accessToken']
        requests.post(f'{URL}{Endpoint.login_user}', data=payload)
        payload["email"] = '111@yandex.ru'
        response_ch_data = requests.patch(f'{URL}{Endpoint.del_and_change_user}', data=payload,
                                          headers={'Authorization': token})
        response_get_data = requests.get(f'{URL}{Endpoint.del_and_change_user}', headers={'Authorization': token})
        assert response_get_data.json()['success'] == True
        assert response_get_data.status_code == 200

    @allure.title('Нельзя изменить данные поля name пользователя предварительно не авторизовавшись')
    @allure.description('Сначала регистрирую пользователя, получаю его токен, изменяю поле name, вывожу результат.'
                        'Для ревьюера: здесь баг, ожидаем код 401, получаем 200 без авторизации')
    def test_changing_data_field_name_without_authorization_code_401(self, generating_the_cour_and_delete_the_cour):
        payload = {"name": generating_the_cour_and_delete_the_cour[0],
                   "email": generating_the_cour_and_delete_the_cour[1],
                   "password": generating_the_cour_and_delete_the_cour[2]}
        res_cr_user = requests.post(f'{URL}{Endpoint.create_user}', data=payload)
        token = res_cr_user.json()['accessToken']
        payload["name"] = '111'
        response_ch_data = requests.patch(f'{URL}{Endpoint.del_and_change_user}', data=payload,
                                          headers={'Authorization': token})
        response_get_data = requests.get(f'{URL}{Endpoint.del_and_change_user}', headers={'Authorization': token})
        assert response_get_data.json()["success"] == True
        assert response_get_data.status_code == 200

    @allure.title('Нельзя изменить данные поля email пользователя предварительно не авторизовавшись')
    @allure.description('Сначала регистрирую пользователя, получаю его токен, изменяю поле email, вывожу результат.'
                        'Для ревьюера: здесь баг, ожидаем код 401, получаем 200 без авторизации')
    def test_changing_data_field_email_without_authorization_code_401(self, generating_the_cour_and_delete_the_cour):
        payload = {"name": generating_the_cour_and_delete_the_cour[0],
                   "email": generating_the_cour_and_delete_the_cour[1],
                   "password": generating_the_cour_and_delete_the_cour[2]}
        res_cr_user = requests.post(f'{URL}{Endpoint.create_user}', data=payload)
        token = res_cr_user.json()['accessToken']
        payload["email"] = '111@yandex.ru'
        response_ch_data = requests.patch(f'{URL}{Endpoint.del_and_change_user}', data=payload,
                                          headers={'Authorization': token})
        response_get_data = requests.get(f'{URL}{Endpoint.del_and_change_user}', headers={'Authorization': token})
        assert response_get_data.json()["success"] == True
        assert response_get_data.status_code == 200

