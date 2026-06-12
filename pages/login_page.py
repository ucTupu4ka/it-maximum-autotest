import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from data.constants import BASE_URL
from data.users import User
from utils.logger import get_logger

logger = get_logger(__name__)


class LoginPage(BasePage):
    URL = BASE_URL + "login"

    HEADER = (By.TAG_NAME, "h2")
    SUBHEADER = (By.TAG_NAME, "h4")

    MESSAGE = (By.ID, "flash-messages")

    USERNAME_FIELD = (By.ID, "username")
    PASSWORD_FIELD = (By.ID, "password")

    LOGIN_BUTTON = (By.TAG_NAME, "button")

    HEADER_TEXT = "Login Page"
    SUBHEADER_TEXT = "This is where you can log into the secure area. "\
                      "Enter tomsmith for the username and SuperSecretPassword! for the password. "\
                      "If the information is wrong you should see error messages."
    LOGIN_BUTTON_TEXT = "Login"

    ERROR_MESSAGE_TEXT = "Your username is invalid!"
    LOGOUT_MESSAGE_TEXT = "You logged out of the secure area!"

    def enter_username(self, user: str):
        field = self.find(self.USERNAME_FIELD)
        field.clear()
        field.send_keys(user)

    def enter_password(self, password: str):
        field = self.find(self.PASSWORD_FIELD)
        field.clear()
        field.send_keys(password)

    def click_login_button(self):
        self.click(self.LOGIN_BUTTON)

    def login(self, user: User):
        with allure.step(f"Login as {user.username}"):
            logger.info("Login as %s", user.username)
            self.enter_username(user.username)
            self.enter_password(user.password)
            self.click_login_button()
