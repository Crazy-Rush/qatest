import pytest

import allure
from test_framework.ui.pages.main_pages.main_page import MainPage


@pytest.mark.ui
@allure.id("C5994515")
@allure.title("C5994515. Появление валидации при введении некорректного пароля")
def test_ui_c5994515_check_password_validation(open_browser):
    # Нажать на поле "Пароль"
    MainPage(open_browser).click_on_the_password_input_field()

    # Проверяем что Лейбл "Пароль" отображается над полем ввода пароля
    MainPage(open_browser).check_the_password_text_above_the_input_field()

    # Ввести невалидный пароль в поле ввода пароля
    MainPage(open_browser).enter_password_in_pass_field(password="1231231")

    # Проверка неактивного статуса кнопки "Войти"
    MainPage(open_browser).check_status_button_login_disabled()

    # Клик на поле ввода телефона
    MainPage(open_browser).click_phone_field()

    # Проверка отображения уведомления о валидации пароля
    MainPage(open_browser).check_message_validation_password()
