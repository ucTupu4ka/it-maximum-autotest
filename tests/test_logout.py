import allure
from pytest_check import check

from pages.login_page import LoginPage
from pages.secure_area_page import SecureAreaPage
from data.users import VALID_USER


@allure.feature("Авторизация")
@allure.story("Выход из системы")
@allure.title("Выход из secure area возвращает на страницу логина")
def test_logout(driver):
    login_page = LoginPage(driver)

    login_page.open()

    login_page.login(VALID_USER)

    secure_page = SecureAreaPage(driver)

    secure_page.click_logout_button()

    check.is_true(login_page.is_opened(), 'Login page is not opened')

    check.equal(login_page.get_text(login_page.MESSAGE)[:-2], login_page.LOGOUT_MESSAGE_TEXT, 'Logout message is not correct')
