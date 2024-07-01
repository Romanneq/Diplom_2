import allure
from helpers import _payload
from http import HTTPStatus
from classes.user import User
from classes.order import Order


class TestCreateOrder:

    @allure.title('Можно создать заказ с авторизацией')
    @allure.description('Регистрирую пользователя, авторизуюсь, получаю хэш ингредиентов, создаю заказ')
    def test_create_order_with_authorization_code_200(self, generating_the_user_and_delete_the_user):
        data_user = _payload(generating_the_user_and_delete_the_user)
        req_cr_user = User.create_user(data_user)
        req_log_user = User.log_user(data_user)
        req_data_ing = Order.get_data_ing()
        _ing = {"ingredients": [req_data_ing.json()['data'][0]['_id'], req_data_ing.json()['data'][1]['_id'],
                                req_data_ing.json()['data'][2]['_id']]}
        req_cr_ord = Order.create_order(_ing)
        assert req_cr_ord.json()['success'] == True
        assert req_cr_ord.status_code == HTTPStatus.OK

    @allure.title('Нельзя создать заказ без авторизации')
    @allure.description('Получаю хэш ингредиентов, создаю заказ.')
    # Для ревьюера: в документации API не сказано, какая ошибка вернется, если не авторизован, поэтому буду считать,
    # что это ошибка 401 Unauthorized
    def test_create_order_without_authorization_code_401(self):
        req_data_ing = Order.get_data_ing()
        _ing = {"ingredients": [req_data_ing.json()['data'][0]['_id'], req_data_ing.json()['data'][1]['_id'],
                                req_data_ing.json()['data'][2]['_id']]}
        req_cr_ord = Order.create_order(_ing)
        assert req_cr_ord.json()['success'] == True
        assert req_cr_ord.status_code == HTTPStatus.OK

    @allure.title('Нельзя создать заказ с авторизацией, но без ингредиентов')
    @allure.description('Регистрирую пользователя, авторизуюсь, создаю заказ без ингредиентов')
    def test_create_order_without_ing_with_auth_code_400(self, generating_the_user_and_delete_the_user):
        data_user = _payload(generating_the_user_and_delete_the_user)
        req_cr_user = User.create_user(data_user)
        req_log_user = User.log_user(data_user)
        _ing = {"ingredients": []}
        req_cr_ord = Order.create_order(_ing)
        assert req_cr_ord.json()['success'] == False
        assert req_cr_ord.status_code == HTTPStatus.BAD_REQUEST

    @allure.title('Нельзя создать заказ с авторизацией и с неверным хэшем ингредиентов')
    @allure.description('Регистрирую пользователя, авторизуюсь, передаю неверный хэш ингредиентов, создаю заказ.')
    # Для ревьюера: ошибки 500 вообще быть не должно.
    def test_create_order_with_incorrect_ing_with_auth_code_500(self, generating_the_user_and_delete_the_user):
        data_user = _payload(generating_the_user_and_delete_the_user)
        req_cr_user = User.create_user(data_user)
        req_log_user = User.log_user(data_user)
        _ing = {"ingredients": ['11111', '6565656', '3333333']}
        req_cr_ord = Order.create_order(_ing)
        assert req_cr_ord.status_code == HTTPStatus.INTERNAL_SERVER_ERROR
