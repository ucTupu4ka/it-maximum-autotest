from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    URL = ""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
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

    def is_element_visible(self, locator) -> bool:
        try:
            self.find(locator)
            return True
        except Exception:
            return False
