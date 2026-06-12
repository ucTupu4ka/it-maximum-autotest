import logging
import allure
from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


logger = logging.getLogger(__name__)


class BasePage:
    """Base class for all pages."""

    URL = ""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        """Open page in browser."""
        with allure.step(f"Open page {self.URL}"):
            logger.info("Open %s", self.URL)
            self.driver.get(self.URL)

    def is_opened(self) -> bool:
        """Check if page is opened."""
        return self.driver.current_url == self.URL

    def find(self, locator):
        """Find element on page."""
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    def click(self, locator):
        """Click on element."""
        self.find(locator).click()

    def get_text(self, locator) -> str:
        """Return element text."""
        return self.find(locator).text

    def get_message_text(self, locator) -> str:
        """Return flash message text without the trailing icon character."""
        return self.get_text(locator).replace("×", "").strip()

    def is_element_visible(self, locator) -> bool:
        """Check if element is visible."""
        try:
            self.find(locator)
            return True
        except TimeoutException:
            logger.warning("Element not found: %s", locator)
            return False
