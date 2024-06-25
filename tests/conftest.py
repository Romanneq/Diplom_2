import random
import string
import pytest
import requests
from data import URL
from data import Endpoint


@pytest.fixture
def generating_the_user_and_delete_the_user():
    # метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    # создаём список, чтобы метод мог его вернуть
    new_user = []

    # генерируем имя, почту и логин пользователя
    name = generate_random_string(5)
    email = f'{generate_random_string(5)}@yandex.ru'
    password = generate_random_string(5)

    # собираем тело запроса
    payload = {
        "name": name,
        "email": email,
        "password": password
    }

    new_user.append(name)
    new_user.append(email)
    new_user.append(password)

    # возвращаем список
    yield new_user

    try:
        login_user = requests.post(f'{URL}{Endpoint.login_user}', data=payload)  # логин user
        token = login_user.json()['accessToken'] # получение accessToken
        del_user = requests.delete(f'{URL}{Endpoint.del_and_change_user}', headers={'Authorization': token})  # удаление user
    except KeyError:
        pass
