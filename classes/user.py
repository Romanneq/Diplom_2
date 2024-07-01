import allure
import requests
from data import URL
from data import Endpoint


class User:

    @allure.title('Создание пользователя')
    @staticmethod
    def create_user(data):
        return requests.post(f'{URL}{Endpoint.CREATE_USER}', data=data)

    @allure.title('логирование user')
    @staticmethod
    def log_user(data):
        return requests.post(f'{URL}{Endpoint.LOGIN_USER}', data=data)

    @allure.title('изменение данных user')
    @staticmethod
    def changing_data_user(data, token):
        return requests.patch(f'{URL}{Endpoint.DEL_AND_CHANGE_USER}', data=data, headers={'Authorization': token})

    @allure.title('получение данных user')
    @staticmethod
    def get_data_user(token):
        return requests.get(f'{URL}{Endpoint.DEL_AND_CHANGE_USER}', headers={'Authorization': token})
