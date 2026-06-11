from pytest_check import check

from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.secure_area_page import SecureAreaPage
from data.users import INVALID_USER
from data.users import VALID_USER


def test_login_page_is_displayed(driver):
    home_page = HomePage(driver)

    home_page.open()

    home_page.click_authorization_form()

    login_page = LoginPage(driver)

    login_page.open()

    check.is_true(login_page.is_opened(), 'Login page is not opened')
    check.equal(login_page.get_text(login_page.HEADER), login_page.HEADER_TEXT, 'Header text is not correct')
    check.equal(login_page.get_text(login_page.SUBHEADER), login_page.SUBHEADER_TEXT, 'Subheader text is not correct')
    check.equal(login_page.get_text(login_page.LOGIN_BUTTON), login_page.LOGIN_BUTTON_TEXT,
                'Login button text is not correct'
                )


def test_invalid_authorization_data(driver):
    login_page = LoginPage(driver)

    login_page.open()

    login_page.login(INVALID_USER)

    check.is_true(login_page.is_element_visible(login_page.MESSAGE), 'Error message is not displayed')
    check.equal(login_page.get_text(login_page.MESSAGE)[:-2], login_page.ERROR_MESSAGE_TEXT,
                'Error message is not correct'
                )

def test_valid_authorization_data(driver):
    login_page = LoginPage(driver)

    login_page.open()

    login_page.login(VALID_USER)

    secure_page = SecureAreaPage(driver)

    check.is_true(secure_page.is_element_visible(secure_page.MESSAGE), 'Success message is not displayed')
    check.equal(secure_page.get_text(secure_page.MESSAGE)[:-2], secure_page.SUCCESS_MESSAGE_TEXT,
                'Error message is not correct'
                )

    check.is_true(secure_page.is_opened(), 'Secure page is not opened')
    check.equal(secure_page.get_text(secure_page.HEADER), secure_page.HEADER_TEXT, 'Header text is not correct')
    check.equal(secure_page.get_text(secure_page.SUBHEADER), secure_page.SUBHEADER_TEXT, 'Subheader text is not correct')
    check.equal(secure_page.get_text(secure_page.LOGOUT_BUTTON), secure_page.LOGOUT_BUTTON_TEXT,
                'Logout button text is not correct'
                )
