# Тестирование API сервиса "Stellar Burgers"
1. Ссылка на сервис: "https://stellarburgers.nomoreparties.site/"
2. Основа для написания автотестов — модуль request
3. Установить зависимости — pip install -r requirements.txt 
4. Проверить, что зависимости установлены: pip freeze
5. Перед каждым тестом генерируется имя, почта, пароль, логирование, удаление user.
6. Фейковая генерация имени, почты, пароля user - helpers/fake_data_user
7. Основные методы работы с классами order и user описаны в директории classes
8. Команда для запуска — run
9. Запустить allure отчет: allure serve allure_results