# Selenium Automation with Pytest
This repository contains a Selenium-based automation framework using Pytest 
for testing web applications. The project aims to provide a robust and 
scalable structure for writing and running automated tests.
## Table of Contents
- [Project Structure](#project-structure)
- [Setup and Installation](#setup-and-installation)
- [Running Tests](#running-tests)
- [Writing Tests](#writing-tests)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)
## Project Structure
selenium-pytest-automation/
│
├── tests/
│ ├── test_login.py
│ ├── test_search.py
│ └── conftest.py
│
├── pages/
│ ├── base_page.py
│ ├── login_page.py
│ └── search_page.py
│
├── utils/
│ └── helpers.py
│
├── reports/
│ └── pytest_report.html
│
├── requirements.txt
├── pytest.ini
├── README.md
└── .gitignore
- `tests/`: Contains test scripts.
- `pages/`: Contains Page Object Model (POM) classes.
- `utils/`: Utility functions and helpers.
- `reports/`: Contains test reports.
- `requirements.txt`: Lists dependencies.
- `pytest.ini`: Pytest configuration.
- `README.md`: Project documentation.
- `.gitignore`: Specifies files to be ignored by Git.
## Setup and Installation
1. **Clone the repository**:
    git clone https://github.com/yourusername/selenium-pytest-automation.git
    cd selenium-pytest-automation
2. **Create a virtual environment** (optional but recommended):
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
3. **Install dependencies**:
    pip install -r requirements.txt
4. **Download WebDriver**:
    Download the WebDriver for the browser you wish to test 
(e.g., ChromeDriver for Chrome) and ensure it is in your PATH.
## Running Tests
Run all tests:
pytest -v -s
## Generate HTML report
pytest --html=reports/pytest_report.html
## Run specific marker
pytest -m smoke

[pytest]
markers =
    login: Tests related to login functionality
    search: Tests related to search functionality
addopts = --maxfail=2 --disable-warnings

## LICENSE
This `README.md` provides a comprehensive guide to set up, run, and 
contribute to the Selenium and Pytest automation project. Adjust the 
repository URL, project details, and test examples to fit your specific 
project needs.

