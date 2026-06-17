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
ui-framework/

│
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   ├── products_page.py
│   ├── cart_page.py
│   └── checkout_page.py
│
├── locators/
│   ├── login_locators.py
│   ├── products_locators.py
│   ├── cart_locators.py
│   └── checkout_locators.py
│
├── tests/
│   ├── test_login.py
│   ├── test_products.py
│   ├── test_cart.py
│   └── test_checkout.py
│
├── utils/
│   ├── waits.py
│   └── logger.py
│
├── conftest.py
├── pytest.ini
└── requirements.txt
'''

## Test Categories

- `smoke` — critical checks, run first
- `positive` — correct usage scenarios
- `negative` — invalid data / error handling