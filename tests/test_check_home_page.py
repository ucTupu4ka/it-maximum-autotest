from pytest_check import check

from pages.home_page import HomePage


def test_home_page_is_displayed(driver):
    home_page = HomePage(driver)

    home_page.open()

    check.is_true(home_page.is_opened(), 'Home page is not opened')
    check.equal(home_page.get_text(home_page.HEADER), home_page.HEADER_TEXT, 'Header text is not correct')
    check.equal(home_page.get_text(home_page.SUBHEADER), home_page.SUBHEADER_TEXT, 'Subheader text is not correct')
    check.equal(home_page.get_text(home_page.AUTHORIZATION_LINK), home_page.AUTHORIZATION_LINK_TEXT,
                'Authorization link is not correct'
                )
