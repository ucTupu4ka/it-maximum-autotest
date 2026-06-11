import pytest

from utils.driver_factory import DriverFactory


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
