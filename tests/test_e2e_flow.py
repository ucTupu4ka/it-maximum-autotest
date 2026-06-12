import allure
from pytest_check import check

from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.secure_area_page import SecureAreaPage
from data.users import INVALID_USER
from data.users import VALID_USER


@allure.feature("Авторизация")
@allure.story("Полный сценарий")
@allure.title("E2E: главная → вход → ошибка → успех → выход")
def test_full_authorization_flow(driver):
    home_page = HomePage(driver)
    login_page = LoginPage(driver)
    secure_page = SecureAreaPage(driver)

    home_page.open()
    check.is_true(home_page.is_opened(), "Home page is not opened")

    home_page.click_authorization_form()
    check.is_true(login_page.is_opened(), "Login page is not opened after clicking the link")

    login_page.login(INVALID_USER)
    check.is_true(login_page.is_element_visible(login_page.MESSAGE), "Error message is not displayed")
    check.equal(
        login_page.get_message_text(login_page.MESSAGE),
        login_page.ERROR_MESSAGE_TEXT,
        "Error message is not correct",
    )

    login_page.login(VALID_USER)
    check.is_true(secure_page.is_opened(), "Secure area is not opened after valid login")
    check.equal(
        secure_page.get_message_text(secure_page.MESSAGE),
        secure_page.SUCCESS_MESSAGE_TEXT,
        "Success message is not correct",
    )

    secure_page.click_logout_button()
    check.is_true(login_page.is_opened(), "Login page is not opened after logout")
    check.equal(
        login_page.get_message_text(login_page.MESSAGE),
        login_page.LOGOUT_MESSAGE_TEXT,
        "Logout message is not correct",
    )
