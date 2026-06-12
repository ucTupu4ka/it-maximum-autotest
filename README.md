# it-maximum-autotest

Автотесты UI для демо-приложения [the-internet.herokuapp.com](https://the-internet.herokuapp.com/).  
Проект покрывает сценарии главной страницы, авторизации, входа с валидными/невалидными данными и выхода из системы.

## Стек технологий

| Категория | Технология |
|-----------|------------|
| Язык | Python 3.12+ |
| Тестовый фреймворк | [pytest](https://docs.pytest.org/) |
| UI-автоматизация | [Selenium WebDriver](https://www.selenium.dev/) |
| Паттерн | Page Object Model |
| Мягкие проверки | [pytest-check](https://github.com/realpython/pytest-check) |
| Отчётность | [Allure Report](https://allure.qatools.ru/) (`allure-pytest`) |
| Управление зависимостями | [Poetry](https://python-poetry.org/) |
| Браузеры | Google Chrome, Mozilla Firefox |

## Структура проекта

```
it-maximum-autotest/
├── conftest.py          # фикстуры pytest, Allure, логирование
├── pytest.ini           # настройки pytest и Allure
├── docs/                # документация и отчёт о тестировании
├── pages/               # Page Object классы
├── tests/               # тестовые сценарии
├── data/                # тестовые данные и константы
└── utils/               # фабрика WebDriver, логгер
```

## Документация

| Документ | Описание |
|----------|----------|
| [docs/TEST_DOCUMENTATION.md](docs/TEST_DOCUMENTATION.md) | Документация тестов: предположения, ограничения, матрица ТЗ → тесты |
| [docs/TEST_REPORT.md](docs/TEST_REPORT.md) | Отчёт о результатах последнего прогона |

---

## Предварительные требования

Перед началом установите:

1. **Git** — [git-scm.com](https://git-scm.com/)
2. **Python 3.12+** — [python.org](https://www.python.org/downloads/)
3. **Poetry** — [установка](https://python-poetry.org/docs/#installation)
4. **Браузер** — Google Chrome или Mozilla Firefox (для Selenium 4 драйвер скачивается автоматически)
5. **Allure CLI** *(опционально, для просмотра HTML-отчёта)*

### Установка Allure CLI

**macOS** (Homebrew):

```bash
brew install allure
```

**Windows** (Scoop):

```powershell
scoop install allure
```

**Windows** (Chocolatey):

```powershell
choco install allure-commandline
```

Либо скачайте архив с [GitHub Releases](https://github.com/allure-framework/allure2/releases) и добавьте `bin` в переменную окружения `PATH`.

---

## Запуск тестов: пошаговая инструкция

### Шаг 1. Клонировать репозиторий

**macOS / Linux** (Terminal):

```bash
git clone https://github.com/ucTupu4ka/it-maximum-autotest.git
cd it-maximum-autotest
```

**Windows** (PowerShell или cmd):

```powershell
git clone <URL-репозитория>
cd it-maximum-autotest
```

### Шаг 2. Установить зависимости Python

В корне проекта выполните (одинаково на macOS и Windows):

```bash
poetry install
```

Poetry создаст виртуальное окружение и установит все пакеты из `pyproject.toml`.

### Шаг 3. Запустить тесты

**macOS / Linux:**

```bash
poetry run pytest
```

**Windows** (PowerShell или cmd):

```powershell
poetry run pytest
```

При успешном прогоне в консоли отобразятся логи тестов, а результаты для Allure сохранятся в папку `allure-results/`.

### Шаг 4. Посмотреть Allure-отчёт *(опционально)*

**macOS / Linux:**

```bash
allure serve allure-results
```

**Windows:**

```powershell
allure serve allure-results
```

Команда откроет отчёт в браузере. Для сохранения статического HTML:

```bash
allure generate allure-results -o allure-report --clean
```

---

## Дополнительные параметры запуска

| Параметр | Описание | Пример |
|----------|----------|--------|
| `--browser` | Браузер: `chrome` или `firefox` (по умолчанию `chrome`) | `poetry run pytest --browser=firefox` |
| `--headless` | Запуск без GUI (включён по умолчанию) | `poetry run pytest --headless` |
| `--log-cli-level` | Уровень логов в консоли | `poetry run pytest --log-cli-level=DEBUG` |

Запуск одного теста или файла:

```bash
poetry run pytest tests/test_login_page.py
poetry run pytest tests/test_login_page.py::test_valid_authorization_data
```

---

## Что проверяют тесты

| Тест | Сценарий |
|------|----------|
| `test_home_page_is_displayed` | Отображение главной страницы |
| `test_login_page_is_displayed` | Переход по ссылке и отображение формы логина |
| `test_invalid_authorization_data` | Ошибка при неверных учётных данных |
| `test_valid_authorization_data` | Успешный вход в secure area |
| `test_logout` | Выход из системы |
| `test_full_authorization_flow` | Полный E2E-сценарий по ТЗ |

При падении теста в Allure автоматически прикрепляется скриншот страницы.
