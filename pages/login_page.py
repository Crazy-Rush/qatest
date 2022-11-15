from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def register_new_user(self, email, password):
        input_email = self.browser.find_element(By.ID, 'id_registration-email')
        input_email.send_keys(email)
        input_password1 = self.browser.find_element(By.ID, 'id_registration-password1')
        input_password1.send_keys(password)
        input_password2 = self.browser.find_element(By.ID, 'id_registration-password2')
        input_password2.send_keys(password)
        registration_button = self.browser.find_element(By.CSS_SELECTOR, '#register_form > button.btn-lg')
        registration_button.click()

    def should_be_login_url(self):
        assert LoginPageLocators.REGIST_FORM_LINK == 'http://selenium1py.pythonanywhere.com/ru/accounts/login/', 'Ссылка не корректна'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Неверно введен селектор формы логина'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'Неверно  введен селектор формы регистрации'