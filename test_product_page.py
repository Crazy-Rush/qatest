import time
import pytest
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.basket_page import BasketPage


@pytest.mark.need_review
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        self.link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        page = LoginPage(browser, self.link)
        page.open()
        page.go_to_login_page()
        page.register_new_user(str(time.time()) + '@fakemail.ru', 'qw12as34zx56')
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        product_page = ProductPage(browser, browser.current_url)
        product_page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
        page.open()
        page.guest_can_add_product_to_basket()
        page.should_be_same_product_name()
        page.guest_can_see_message_add_basket()
        page.should_be_same_total_price()
        page.guest_can_see_basket_price()

@pytest.mark.need_review
class TestGuestAddToBasketFromProductPage():
    def test_guest_can_add_product_to_basket(self, browser):
        product_page = ProductPage(browser, 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019.')
        product_page.open()
        product_page.go_to_product_page()
        product_page.solve_quiz_and_get_code()
        product_page.guest_can_see_basket_price()
        product_page.guest_can_see_message_add_basket()
        product_page.should_be_same_product_name()
        product_page.should_be_same_total_price()
        time.sleep(5)

    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/'
        page = ProductPage(browser, link)
        page.open()
        page.go_to_basket_page_from_header()
        new_page = BasketPage(browser, browser.current_url)
        new_page.should_be_empty_basket_message()
        new_page.should_not_be_product_in_empty_basket()


    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()
        page.go_to_login_page()

    def test_guest_should_see_login_link_on_product_page(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()


