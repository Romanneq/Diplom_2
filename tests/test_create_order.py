import allure
import requests
from data import URL
from data import Endpoint


class TestCreateOrder:

    @allure.title('Можно создать заказ с авторизацией')
    @allure.description('Регистрирую пользователя, авторизуюсь, получаю хэш ингредиентов, создаю заказ')
    def test_create_order_with_authorization_code_200(self, generating_the_cour_and_delete_the_cour):
        payload = {"name": generating_the_cour_and_delete_the_cour[0],
                   "email": generating_the_cour_and_delete_the_cour[1],
                   "password": generating_the_cour_and_delete_the_cour[2]}
        res_cr_user = requests.post(f'{URL}{Endpoint.create_user}', data=payload)
        requests.post(f'{URL}{Endpoint.login_user}', data=payload)
        response_data_ing = requests.get(f'{URL}{Endpoint.data_ing}')
        _ing = {"ingredients": [response_data_ing.json()['data'][0]['_id'], response_data_ing.json()['data'][1]['_id'],
                                response_data_ing.json()['data'][2]['_id']]}
        res_cr_ord = requests.post(f'{URL}{Endpoint.create_and_get_order}', data=_ing)
        assert res_cr_ord.json()['success'] == True
        assert res_cr_ord.status_code == 200

    @allure.title('Нельзя создать заказ без авторизации')
    @allure.description('Получаю хэш ингредиентов, создаю заказ. Для ревьюера: в документации API не сказано, '
    'какая ошибка вернется, если не авторизован, поэтому буду считать, что это ошибка 401 Unauthorized')
    def test_create_order_without_authorization_code_401(self):
        response_data_ing = requests.get(f'{URL}{Endpoint.data_ing}')
        _ing = {"ingredients": [response_data_ing.json()['data'][0]['_id'], response_data_ing.json()['data'][1]['_id'],
                                response_data_ing.json()['data'][2]['_id']]}
        res_cr_ord = requests.post(f'{URL}{Endpoint.create_and_get_order}', data=_ing)
        assert res_cr_ord.json()['success'] == True
        assert res_cr_ord.status_code == 200

    @allure.title('Нельзя создать заказ с авторизацией, но без ингредиентов')
    @allure.description('Регистрирую пользователя, авторизуюсь, создаю заказ без ингредиентов')
    def test_create_order_without_ing_with_auth_code_400(self, generating_the_cour_and_delete_the_cour):
        payload = {"name": generating_the_cour_and_delete_the_cour[0],
                   "email": generating_the_cour_and_delete_the_cour[1],
                   "password": generating_the_cour_and_delete_the_cour[2]}
        res_cr_user = requests.post(f'{URL}{Endpoint.create_user}', data=payload)
        requests.post(f'{URL}{Endpoint.login_user}', data=payload)
        _ing = {"ingredients": []}
        res_cr_ord = requests.post(f'{URL}{Endpoint.create_and_get_order}', data=_ing)
        assert res_cr_ord.json()['success'] == False
        assert res_cr_ord.status_code == 400

    @allure.title('Нельзя создать заказ с авторизацией и с неверным хэшем ингредиентов')
    @allure.description('Регистрирую пользователя, авторизуюсь, передаю неверный хэш ингредиентов, создаю заказ. '
                        'Для ревьюера: в документации к API ошибки 500 вообще быть не должно.')
    def test_create_order_with_incorrect_ing_with_auth_code_500(self, generating_the_cour_and_delete_the_cour):
        payload = {"name": generating_the_cour_and_delete_the_cour[0],
                   "email": generating_the_cour_and_delete_the_cour[1],
                   "password": generating_the_cour_and_delete_the_cour[2]}
        res_cr_user = requests.post(f'{URL}{Endpoint.create_user}', data=payload)
        requests.post(f'{URL}{Endpoint.login_user}', data=payload)
        _ing = {"ingredients": ['11111', '6565656', '3333333']}
        res_cr_ord = requests.post(f'{URL}{Endpoint.create_and_get_order}', data=_ing)
        assert res_cr_ord.status_code == 500


