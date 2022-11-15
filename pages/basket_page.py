from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket_message(self):
        basket_message = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_MESSAGE).text
        assert 'Your basket is empty.' in basket_message, 'Должно быть сообщение о пустой корзине'

    def should_not_be_product_in_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IN_BASKET_ROW), 'Товара в корзине быть не должно'
