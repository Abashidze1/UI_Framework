# UI Automation Framework

Automation framework for testing [Sauce Demo](https://www.saucedemo.com/) web application.

## Tech Stack

- **Python**
- **Selenium** — browser automation
- **Pytest** — test runner
- **Page Object Model** — test architecture pattern
- **Loguru** — logging
- **webdriver-manager** — automatic driver management

## Структура проекта

```text
api-framework/
├── clients/
│   ├── base_client.py       # Базовые HTTP методы + автоматическое логирование
│   ├── posts_client.py      # Эндпоинты /posts
│   └── users_client.py      # Эндпоинты /users
├── models/
│   ├── post_model.py        # Pydantic-схема для ответа Post
│   └── user_model.py        # Pydantic-схема для ответа User (вложенные объекты)
├── data/
│   └── test_data.py         # Тестовые данные для параметризации
├── utils/
│   └── logger.py            # Конфигурация логгера (loguru)
├── tests/
│   ├── posts/               # Тесты для /posts (smoke, positive, negative)
│   └── users/               # Тесты для /users
├── conftest.py              # Глобальные фикстуры (инициализация API-клиентов)
├── pytest.ini               # Конфигурация Pytest (маркеры, логи)
└── requirements.txt         # Зависимости проекта

```
## Test Categories

- `smoke` — critical checks, run first
- `positive` — correct usage scenarios
- `negative` — invalid data / error handling
