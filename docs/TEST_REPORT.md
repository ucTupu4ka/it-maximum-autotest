# Отчёт о результатах тестирования

## Сводка

| Параметр | Значение |
|----------|----------|
| Дата прогона | 12.06.2026 |
| Окружение | macOS, Python 3.14.5 |
| Браузер | Google Chrome (headless) |
| Команда запуска | `poetry run pytest` |
| Всего тестов | 6 |
| Passed | 6 |
| Failed | 0 |
| Skipped | 0 |
| Время выполнения | 27.04 с |

**Итог: все тесты пройдены успешно.**

---

## Результаты по тестам

| # | Тест | Статус | Время* |
|---|------|--------|--------|
| 1 | `test_home_page_is_displayed` | PASSED | ~3 с |
| 2 | `test_full_authorization_flow` | PASSED | ~6 с |
| 3 | `test_login_page_is_displayed` | PASSED | ~4 с |
| 4 | `test_invalid_authorization_data` | PASSED | ~4 с |
| 5 | `test_valid_authorization_data` | PASSED | ~5 с |
| 6 | `test_logout` | PASSED | ~5 с |

\*Приблизительное время на один тест (включая создание браузера).

---

## Проверенные сценарии

### Главная страница
- URL соответствует `https://the-internet.herokuapp.com/`
- Заголовки и ссылка «Form Authentication» отображаются корректно

### Авторизация
- Переход на страницу логина по клику на ссылку с главной
- При вводе `test` / `test` отображается ошибка «Your username is invalid!»
- При вводе `tomsmith` / `SuperSecretPassword!` открывается Secure Area
- Сообщение об успешном входе: «You logged into a secure area!»

### Выход
- Кнопка Logout возвращает на страницу логина
- Сообщение: «You logged out of the secure area!»

### E2E
- Сквозной сценарий от главной страницы до выхода выполнен без ошибок

---

## Вывод pytest (фрагмент)

```
tests/test_check_home_page.py::test_home_page_is_displayed PASSED       [ 16%]
tests/test_e2e_flow.py::test_full_authorization_flow PASSED               [ 33%]
tests/test_login_page.py::test_login_page_is_displayed PASSED             [ 50%]
tests/test_login_page.py::test_invalid_authorization_data PASSED           [ 66%]
tests/test_login_page.py::test_valid_authorization_data PASSED             [ 83%]
tests/test_logout.py::test_logout PASSED                                 [100%]

============================== 6 passed in 27.04s ==============================
```

---

## Allure-отчёт

После прогона результаты доступны в каталоге `allure-results/`.

Для просмотра интерактивного отчёта:

```bash
allure serve allure-results
```

Для генерации статического HTML:

```bash
allure generate allure-results -o allure-report --clean
```

В Allure-отчёте доступны:
- группировка по feature/story;
- шаги «Open page …» и «Login as …»;
- скриншот страницы при падении теста (в данном прогоне падений не было).

---

## Замечания

Дефектов по результатам прогона не обнаружено.  
При повторном запуске на другой ОС или в Firefox рекомендуется обновить данный отчёт командой:

```bash
poetry run pytest --browser=firefox
```
