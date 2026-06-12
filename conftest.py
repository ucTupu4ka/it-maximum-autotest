import logging

import allure
import pytest

from utils.driver_factory import DriverFactory
from utils.logger import get_logger


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
        default=True,
        help="Run browser in headless mode",
    )


def pytest_configure(config):
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)-7s | %(name)s | %(message)s",
        datefmt="%H:%M:%S",
    )


@pytest.fixture(autouse=True)
def log_test_boundaries(request):
    log = get_logger("test")
    log.info("START %s", request.node.name)
    yield
    log.info("END %s", request.node.name)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    setattr(item, f"rep_{report.when}", report)


@pytest.fixture(scope="function")
def driver(request):
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")

    log = get_logger("driver")
    log.info("Creating driver: browser=%s, headless=%s", browser, headless)

    driver = DriverFactory.create_driver(
        browser=browser,
        headless=headless,
    )

    yield driver

    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        allure.attach(
            driver.get_screenshot_as_png(),
            name="screenshot",
            attachment_type=allure.attachment_type.PNG,
        )

    driver.quit()
