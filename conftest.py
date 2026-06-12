import logging

import allure
import pytest

from utils.driver_factory import DriverFactory

logger = logging.getLogger(__name__)


def pytest_addoption(parser):
    """Add command line options."""
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser name: chrome or firefox",
    )

    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Run browser in headless mode",
    )


@pytest.fixture(autouse=True)
def log_test_boundaries(request):
    """Fixture for logging test boundaries."""
    logger.info("START %s", request.node.name)
    yield
    logger.info("END %s", request.node.name)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook  for make report if test failed."""
    outcome = yield
    report = outcome.get_result()
    setattr(item, f"rep_{report.when}", report)


@pytest.fixture(scope="function")
def driver(request):
    """Driver fixture."""
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")

    logger.info("Creating driver: browser=%s, headless=%s", browser, headless)

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
