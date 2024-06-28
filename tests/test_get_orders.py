import allure
import requests
from data import URL
from data import Endpoint


class TestLoginUser:

    @allure.title('Можно получить заказы авторизованного пользователя')
    @allure.description('Создаю пользователя, авторизуюсь, получаю токен, создаю заказ (в ручку передаю токен), '
                        'затем получаю список заказов. Для ревьюера: есть разница в ответе: '
                        'в документации к API ключа "name" нет, нарушен порядок ключей. Также в документации API '
                        'ничего не сказано про передачу токена авторизации в ручку создания заказа для отображения '
                        'заказа у пользователя')
    def test_get_orders_user_with_authorization_code_200(self, generating_the_user_and_delete_the_user):
        payload = {"name": generating_the_user_and_delete_the_user[0],
                   "email": generating_the_user_and_delete_the_user[1],
                   "password": generating_the_user_and_delete_the_user[2]}
        res_cr_user = requests.post(f'{URL}{Endpoint.create_user}', data=payload)
        res_log = requests.post(f'{URL}{Endpoint.login_user}', data=payload)
        token = res_log.json()['accessToken']
        res_ing = response_data_ing = requests.get(f'{URL}{Endpoint.data_ing}')
        _ing = {"ingredients": [response_data_ing.json()['data'][0]['_id'], response_data_ing.json()['data'][1]['_id'],
                                response_data_ing.json()['data'][2]['_id']]}
        res_cr_ord = requests.post(f'{URL}{Endpoint.create_and_get_order}', data=_ing,
                                   headers={'Authorization': token})
        res_get_orders = requests.get(f'{URL}{Endpoint.create_and_get_order}', headers={'Authorization': token})
        print(res_get_orders.json()) # Для ревьюера: здесь я написал метод print для отображения ответа в allure-отчёте
        assert res_get_orders.json()['success'] == True
        assert res_get_orders.status_code == 200

    @allure.title('Нельзя получить заказы неавторизованного пользователя')
    def test_get_orders_unauthorized_user_code_401(self):
        res_get_orders = requests.get(f'{URL}{Endpoint.create_and_get_order}')
        assert res_get_orders.json()['success'] == False
        assert res_get_orders.status_code == 401