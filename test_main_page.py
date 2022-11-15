import pytest
from pages.main_page import MainPage
from pages.locators import MainPageLocators, LoginPageLocators, ProductPageLocators
from pages.login_page import LoginPage
from pages.basket_page import BasketPage

@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, MainPageLocators.LINK)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, MainPageLocators.LINK)
        page.open()
        page.should_be_login_link()


class TestGuestCanRegister():
    def test_guest_should_see_registration_form(swlf, browser):

        registration_page = LoginPage(browser, LoginPageLocators.REGIST_FORM_LINK)
        registration_page.open()
        registration_page.should_be_login_url()

    def test_guest_should_be_login_form(swlf, browser):

        registration_page = LoginPage(browser, LoginPageLocators.REGIST_FORM_LINK)
        registration_page.open()
        registration_page.should_be_login_form()

    def test_guest_should_be_registration_form(self, browser):
        registration_page = LoginPage(browser, LoginPageLocators.REGIST_FORM_LINK)
        registration_page.open()
        registration_page.should_be_register_form()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPage(browser, MainPageLocators.LINK)
    page.open()
    page.go_to_basket_page_from_header()
    new_page = BasketPage(browser, browser.current_url)
    new_page.should_be_empty_basket_message()
    new_page.should_not_be_product_in_empty_basket()
