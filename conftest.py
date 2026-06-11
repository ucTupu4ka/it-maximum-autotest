import os
from pathlib import Path

import pytest

from utils.driver_factory import DriverFactory
from pages.login_page import LoginPage
from pages.secure_area_page import SecureAreaPage

from data.users import VALID_USER


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser name: chrome or firefox",
    )

    parser.addoption(
        "--headless",
        action="store_true",
        help="Run browser in headless mode",
    )


@pytest.fixture(scope="function")
def driver(request):
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")

    driver = DriverFactory.create_driver(
        browser=browser,
        headless=headless,
    )

    yield driver

    driver.quit()


@pytest.fixture
def login_page(driver):
    page = LoginPage(driver)
    page.open()
    return page


@pytest.fixture
def authorized_user(driver):
    login_page = LoginPage(driver)
    login_page.open()

    login_page.login(VALID_USER)

    return SecureAreaPage(driver)


@pytest.fixture(scope="session")
def base_url():
    return "https://the-internet.herokuapp.com"