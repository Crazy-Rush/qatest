from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LINK = "http://selenium1py.pythonanywhere.com/"
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '#content_inner > article > div:nth-child(1) > div:nth-child(2) > p:nth-child(2)')


class LoginPageLocators():
    REGIST_FORM_LINK = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators():
    PRODUCT_PAGE_LINK = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'
    PUT_TO_BASKET_BUTTON = (By.CSS_SELECTOR, '.btn-primary.btn-add-to-basket')
    PRODUCT_ADD_BASKET_MESSAGE = (By.CSS_SELECTOR, '#messages > div:nth-child(1).alert-success.alert-safe')
    PRODUCT_NAME_AT_MESSAGE = (By.CSS_SELECTOR, '#messages > div:nth-child(1) > div > strong')
    BASKET_PRICE_MESSAGE = (By.CSS_SELECTOR, '#messages > div:nth-child(3) >div >p:nth-child(1)')
    BASKET_PRICE = (By.CSS_SELECTOR, '#messages > div:nth-child(3) >div >p:nth-child(1) > strong')


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, '#default > header >div:nth-child(1) > div > div:nth-child(2) >span')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    BASKET_EMPTY_MESSAGE = (By.CSS_SELECTOR, '#content_inner > p')
    PRODUCT_IN_BASKET_ROW = (By.CSS_SELECTOR, '#content_inner > form > div.basket-items')



