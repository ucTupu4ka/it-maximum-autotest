import allure
from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.logger import get_logger

logger = get_logger(__name__)


class BasePage:
    URL = ""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        with allure.step(f"Open page {self.URL}"):
            logger.info("Open %s", self.URL)
            self.driver.get(self.URL)

    def is_opened(self) -> bool:
        return self.driver.current_url == self.URL

    def find(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    def click(self, locator):
        self.find(locator).click()

    def get_text(self, locator) -> str:
        return self.find(locator).text

    def get_message_text(self, locator) -> str:
        """Return flash message text without the trailing icon character."""
        return self.get_text(locator).replace("×", "").strip()

    def is_element_visible(self, locator) -> bool:
        try:
            self.find(locator)
            return True
        except TimeoutException:
            logger.warning("Element not found: %s", locator)
            return False
