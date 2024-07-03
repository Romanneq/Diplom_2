import allure
from http import HTTPStatus
from helpers import _payload
from classes.user import User
from classes.order import Order


class TestLoginUser:

    @allure.title('Можно получить заказы авторизованного пользователя')
    @allure.description('Создаю пользователя, авторизуюсь, получаю токен, создаю заказ (в ручку передаю токен), '
                        'затем получаю список заказов.')
    # Для ревьюера: есть разница в ответе: в документации к API ключа "name" нет, нарушен порядок ключей.
    # Также в документации API ничего не сказано про передачу токена авторизации в ручку создания заказа
    # для отображения заказа у пользователя
    def test_get_orders_user_with_authorization_code_200(self, generating_the_user_and_delete_the_user):
        data_user = _payload(generating_the_user_and_delete_the_user)
        req_cr_user = User.create_user(data_user)
        req_log_user = User.log_user(data_user)
        token = req_log_user.json()['accessToken']
        req_data_ing = Order.get_data_ing()
        _ing = {"ingredients": [req_data_ing.json()['data'][0]['_id'], req_data_ing.json()['data'][1]['_id'],
                                req_data_ing.json()['data'][2]['_id']]}
        req_cr_ord = Order.create_order_user(_ing, token)
        req_get_orders = Order.get_orders_user(token)
        print(req_get_orders.json())  # Для ревьюера: здесь я написал метод print для отображения ответа в allure-отчёте
        assert req_get_orders.json()['success'] == True
        assert req_get_orders.status_code == HTTPStatus.OK

    @allure.title('Нельзя получить заказы без авторизованного пользователя')
    def test_get_orders_unauthorized_user_code_401(self):
        req_get_orders = Order.not_get_orders_user()
        assert req_get_orders.json()['success'] == False
        assert req_get_orders.status_code == HTTPStatus.UNAUTHORIZED
