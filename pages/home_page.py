from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from data.constants import BASE_URL


class HomePage(BasePage):
    URL = BASE_URL

    HEADER = (By.TAG_NAME, "h1")
    SUBHEADER = (By.TAG_NAME, "h2")
    AUTHORIZATION_LINK = (By.LINK_TEXT, "Form Authentication")

    HEADER_TEXT = "Welcome to the-internet"
    SUBHEADER_TEXT = "Available Examples"
    AUTHORIZATION_LINK_TEXT = "Form Authentication"

    def click_authorization_form(self):
        self.click(self.AUTHORIZATION_LINK)
