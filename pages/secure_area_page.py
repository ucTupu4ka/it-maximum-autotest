from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from data.constants import BASE_URL


class SecureAreaPage(BasePage):
    """Secure area page."""

    URL = BASE_URL + "secure"

    MESSAGE = (By.ID, "flash")

    HEADER = (By.TAG_NAME, "h2")
    SUBHEADER = (By.TAG_NAME, "h4")

    LOGOUT_BUTTON = (By.LINK_TEXT, "Logout")

    HEADER_TEXT = "Secure Area"
    SUBHEADER_TEXT = "Welcome to the Secure Area. When you are done click logout below."

    LOGOUT_BUTTON_TEXT = "Logout"
    SUCCESS_MESSAGE_TEXT = "You logged into a secure area!"

    def click_logout_button(self):
        """Click logout button."""
        self.click(self.LOGOUT_BUTTON)
