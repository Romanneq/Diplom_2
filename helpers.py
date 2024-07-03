import faker


def _payload(generating_the_user_and_delete_the_user):
    payload = {"name": generating_the_user_and_delete_the_user[0],
               "email": generating_the_user_and_delete_the_user[1],
               "password": generating_the_user_and_delete_the_user[2]}
    return payload


def fake_data_user():
    fake = faker.Faker()
    fake_name = fake.first_name()[0:5]
    fake_email = f'{fake.email()[0:5]}@yandex.ru'
    fake_password = fake.password()[0:5]
    return fake_name, fake_email, fake_password
