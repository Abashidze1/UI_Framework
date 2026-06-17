# UI Automation Framework

Automation framework for testing [Sauce Demo](https://www.saucedemo.com/) web application.

## Tech Stack

- **Python**
- **Selenium** — browser automation
- **Pytest** — test runner
- **Page Object Model** — test architecture pattern
- **Loguru** — logging
- **webdriver-manager** — automatic driver management

## Project Structure
'''
api-framework/

│

├── clients/

│   ├── base_client.py    # base HTTP methods + automatic logging

│   ├── posts_client.py   # /posts endpoints

│   └── users_client.py   # /users endpoints

│

├── models/

│   ├── post_model.py     # Pydantic schema for Post response

│   └── user_model.py     # Pydantic schema for User response (nested objects)

│

├── data/

│   └── test_data.py      # test data for parametrization

│

├── utils/

│   └── logger.py         # loguru configuration

│

├── tests/

│   ├── posts/            # smoke, positive, negative, parametrized

│   └── users/

│

├── conftest.py           # shared fixtures (API clients)

├── pytest.ini            # markers and logging config

└── requirements.txt
'''

## Test Categories

- `smoke` — critical checks, run first
- `positive` — correct usage scenarios
- `negative` — invalid data / error handling
