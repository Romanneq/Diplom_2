# Тестирование API сервиса "Stellar Burgers"
1. Ссылка на сервис: "https://stellarburgers.nomoreparties.site/"
2. Основа для написания автотестов — модуль request
3. Установить зависимости — pip install -r requirements.txt 
4. Проверить, что request,json, pytest, allure установлены: pip freeze
5. Перед каждым тестом генерируется имя,почта, пароль user, логирование, удаление user. 
6. Фикстура находится в tests/conftest.py, метод generating_the_user_and_delete_the_user()
7. Команда для запуска — run
8. Запустить allure отчет: allure serve allure_results
9. Для ревьюера: баги, расхожесть с документацией API в allure-отчёте написаны в декораторе @allure.description
