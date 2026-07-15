# 🛒 Automated Testing of SauceDemo E-commerce Web Application

##  Project Overview

This project automates the testing of the SauceDemo E-commerce web application using **Python**, **Selenium WebDriver**, **Pytest**, and the **Page Object Model (POM)** design pattern.

The framework validates the application's core functionalities such as login, logout, product selection, cart operations, checkout, sorting, and application state reset. It also generates detailed execution reports using **Allure Report**.

**Application Under Test:** https://www.saucedemo.com/

---

#  Project Objective

The objective of this project is to automate the testing of the SauceDemo web application by simulating real user interactions and validating the application's behavior.

The framework is designed to:

- Automate end-to-end user workflows
- Validate functional correctness
- Improve test reusability and maintainability
- Generate detailed execution reports
- Demonstrate industry-standard automation practices

---

# 🛠 Technologies Used

| Technology | Purpose |
|------------|---------|
| Python 3.10 | Programming Language |
| Selenium WebDriver | Browser Automation |
| Pytest | Test Execution Framework |
| Allure Report | Test Reporting |
| WebDriver Manager | Automatic Driver Management |
| JSON | Test Data Management |
| Chrome Browser | Test Execution |

---

#  Project Structure

```
SauceDemo_Automation/
│
├── data/
│   ├── checkout_data.json
│   ├── invalid_users.json
│   └── users.json
│
├── logs/
│
├── pages/
│   ├── base_page.py
│   ├── cart_page.py
│   ├── checkout_page.py
│   ├── inventory_page.py
│   ├── login_page.py
│   └── menu_page.py
│
├── reports/
│
├── screenshots/
│
├── tests/
│   ├── test_add_to_cart.py
│   ├── test_cart_icon.py
│   ├── test_cart_validation.py
│   ├── test_checkout.py
│   ├── test_invalid_login.py
│   ├── test_login.py
│   ├── test_logout.py
│   ├── test_random_products.py
│   ├── test_reset_app.py
│   └── test_sort.py
│
├── utilities/
│   ├── driver_factory.py
│   ├── json_reader.py
│   ├── logger.py
│   └── screenshot.py
│
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

---

# 🏗 Framework Design

The framework follows the **Page Object Model (POM)** architecture.

### Page Objects

- LoginPage
- InventoryPage
- CartPage
- CheckoutPage
- MenuPage
- BasePage

### Utilities

- DriverFactory
- JsonReader
- Logger
- Screenshot Utility

---

# 📋 Test Scenarios

| Test Case | Description | Status |
|------------|-------------|--------|
| TC01 | Login with predefined users | Done   |
| TC02 | Login with invalid credentials | Done   |
| TC03 | Logout functionality | Done   |
| TC04 | Cart icon visibility | Done   |
| TC05 | Random product selection | Done   |
| TC06 | Add products to cart | Done   |
| TC07 | Validate cart contents | Done   |
| TC08 | Complete checkout | Done   |
| TC09 | Product sorting | Done   |
| TC10 | Reset App State | Done   |

**Total Test Cases Executed:** 19

**Execution Result:** 19 Passed

---

# ▶ Installation

Clone the repository

```bash
git clone <repository_url>
```

Navigate to the project

```bash
cd SauceDemo_Automation
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate virtual environment

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶ Running Tests

Execute all test cases

```bash
pytest
```

Execute with verbose output

```bash
pytest -v
```

Generate Allure results

```bash
pytest --alluredir=reports
```

Generate Allure Report

```bash
allure generate reports -o allure-report --clean
```

Open Allure Report

```bash
allure open allure-report
```

---

# 📊 Reporting

The framework generates:

- Allure HTML Report
- Console Execution Report
- Log Files
- Failure Screenshots

---

# ⭐ Features

- Page Object Model (POM)
- Data-Driven Testing using JSON
- Reusable Components
- Explicit Waits
- Exception Handling
- Logging
- Screenshot Capture
- Random Product Selection
- Cart Validation
- Checkout Validation
- Sorting Validation
- Reset Application State Validation
- Allure Reporting

---

# Framework Highlights

- Modular Architecture
- Object-Oriented Design
- Easy Maintenance
- Reusable Page Objects
- Clean Code Structure
- Industry Standard Automation Practices

---

