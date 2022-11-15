from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    def should_be_product_page(self):
        self.guest_can_add_product_to_basket()
        self.go_to_product_page()
        self.should_be_same_total_price()
        self.guest_can_see_message_add_basket()
        self.should_be_same_product_name()
        self.guest_can_see_basket_price()

    def go_to_product_page(self):
        product_page_button = self.browser.find_element(By.CSS_SELECTOR, '.btn-primary.btn-add-to-basket')
        product_page_button.click()

    def guest_can_add_product_to_basket(self):
        button_add_product = self.browser.find_element(*ProductPageLocators.PUT_TO_BASKET_BUTTON)
        button_add_product.click()
        assert self.is_element_present(*ProductPageLocators.PUT_TO_BASKET_BUTTON), 'Неверно указан селектор кнопки добавления в карзину'


    def should_be_same_product_name(self):
        name_in_main = self.browser.find_element(By.CSS_SELECTOR, '.product_main h1').text
        name_in_basket = self.browser.find_element(By.CSS_SELECTOR, '#messages > div:nth-child(1) > div > strong').text
        assert name_in_main == name_in_basket, 'Название товара в корзине не совпадает с названием на странице товара'

    def should_be_same_total_price(self):
        price_in_main = self.browser.find_element(By.CSS_SELECTOR, '#content_inner > article > div:nth-child(1) > div:nth-child(2) > p:nth-child(2)').text
        price_in_basket = self.browser.find_element(By.CSS_SELECTOR, '#messages > div:nth-child(3) >div >p:nth-child(1) > strong').text
        assert price_in_main == price_in_basket, 'Цена товара в корзине не равна цене с главной страницы'

    def guest_can_see_message_add_basket(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_ADD_BASKET_MESSAGE), 'Отсутствует сообщение о добавлении товара в корзину'

    def guest_can_see_basket_price(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_PRICE_MESSAGE), 'Отсутсвтует цена товара в корзине'


    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_ADD_BASKET_MESSAGE),  \
            "Success message is presented, but should not be"


    def should_not_be_success_message_dissapear(self):
        assert self.is_disappeared(*ProductPageLocators.PRODUCT_ADD_BASKET_MESSAGE), \
            "Success message is presented, but should not be"