from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from data.constants import BASE_URL
from data.users import User


class LoginPage(BasePage):
    URL = BASE_URL + "login"

    HEADER = (By.TAG_NAME, "h2")
    SUBHEADER = (By.TAG_NAME, "h4")

    USERNAME_FIELD = (By.ID, "username")
    PASSWORD_FIELD = (By.ID, "password")

    LOGIN_BUTTON = (By.ID, "login")

    HEADER_TEXT = "Login Page"
    SUBHEADER_TEXT = "This is where you can log into the secure area."\
                      "Enter tomsmith for the username and SuperSecretPassword! for the password. "\
                      "If the information is wrong you should see error messages."

    LOGIN_BUTTON_TEXT = "Login"

    def enter_username(self, user: str):
        self.find(self.USERNAME_FIELD).send_keys(user)

    def enter_password(self, password: str):
        self.find(self.PASSWORD_FIELD).send_keys(password)

    def click_login_button(self):
        self.click(self.LOGIN_BUTTON)

    def login(self, user: User):
        self.enter_username(user.username)
        self.enter_password(user.password)
        self.click_login_button()


