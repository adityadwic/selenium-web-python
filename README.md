# Automation Testing Portfolio

## Description

Welcome to my **Automation Testing Portfolio**! This project represents my skills and experience as a **Quality Assurance (QA) Engineer** in the field of software test automation. In this portfolio, you will find various scripts and frameworks I have created using **Selenium** and **Python** to automate web application testing.

The goal of this project is to demonstrate my ability to design and implement efficient, maintainable, and scalable test automation solutions. Each test script is designed to test various aspects of a web application, such as user registration, login, product search, and more, with a systematic and structured approach.

This project also includes the implementation of several commonly used testing frameworks, such as:

- **Page Object Model (POM)**: A design pattern to organize page elements and interactions within an application in a structured way that promotes readability and maintainability of the code.
- **Data-Driven Testing**: Using external files (such as CSV, Excel, or JSON) to test various data sets on the application, providing more flexibility in testing.
- **Linear Testing**: A direct approach to functional testing where test steps are executed sequentially without any specific structure, but still demonstrating effective testing principles.

Through this portfolio, I aim to showcase my ability to design reliable, maintainable, and scalable automation test frameworks for web applications. Each test is optimized to speed up the software testing cycle, reduce bugs, and improve the overall product quality.

## Features

- **Selenium WebDriver** with Python to automate web application testing.
- **Page Object Model (POM)** to organize page elements and interactions in a structured and reusable way.
- **Data-Driven Testing** with external files (such as CSV, Excel, or JSON) to test various inputs and data.
- **Keyword-Driven Testing** and **Behavior-Driven Testing (BDD)** (if applied in specific projects).
- Various types of tests, including user registration, user login, product search, and more.

## Technologies Used

- **Selenium WebDriver**: The main framework for automating web application testing.
- **Python**: The primary programming language for writing automation scripts.
- **pytest**: A testing framework for writing and executing tests.
- **webdriver-manager**: For managing browser drivers automatically.
- **POM (Page Object Model)**: The design pattern used to organize web application tests.

## Project Structure

```plaintext
automation-framework/
│
├── tests/                       # Folder for test cases
│   ├── pom_test_registration.py # Test case for user registration
│   ├── pom_test_login.py        # Test case for user login
│   ├── pom_test_search_product.py # Test case for searching products
│
├── pages/                        # Folder for Page Object Model
│   ├── home_page.py              # Class for the Home page
│   ├── signup_page.py            # Class for the Sign Up page
│   ├── login_page.py             # Class for the Login page
│   ├── products_page.py          # Class for the Products page
│
├── drivers/                      # Folder for WebDriver (for Chrome, Firefox, etc.)
│   └── chromedriver.exe
│
├── utilities/                    # Folder for additional utilities
│   └── driver_factory.py         # For managing WebDriver initialization
│
└── requirements.txt              # File for dependencies
```

## Instalasi

To get started with this project, follow these simple steps:

1. Clone this repository to your local machine:

```bash
git clone https://github.com/username/automation-testing-portfolio.git
cd automation-testing-portfolio
```
2. Install the required dependencies using pip:

```pip install -r requirements.txt```

3.	Run the tests using pytest:

```pytest tests/```

## Tests

The tests will run across all files in the `tests/` folder.

## How to Add a New Test

To add a new test to the project, follow these steps:

1. Create a new test file in the `tests/` folder and follow the existing test patterns.
2. Create a new class in the `pages/` folder for each relevant new page.
3. Write the test case using the **Page Object Model (POM)** approach to ensure the code remains maintainable.
4. Run pytest to ensure all tests pass successfully.

## Contribution

If you’d like to contribute to this project, you can follow these steps:

1. Fork this repository.
2. Create a new branch for the feature or fix you want to add.
3. After completing your work, create a pull request to discuss your changes.

Make sure to follow the existing coding guidelines and write automated tests for every change you make.

## Author

- Your Name: [LinkedIn Aditya Dwi Cahyono](https://www.linkedin.com/in/adityadwicahyono/) | [GitHub](https://github.com/adityadwic)
