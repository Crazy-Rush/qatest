import pytest

import allure
from test_framework.ui.data.user_data import valid_password, valid_phone_number_ui_python
from test_framework.ui.pages.main_pages.main_page import MainPage


@pytest.mark.ui
@allure.id("C5992946")
@allure.title("C5992946. Авторизация по номеру телефона с валидными данными")
def test_ui_c5992946_authorization_by_phone_valid(open_browser):
    # Нажать на кнопку "По телефону"
    MainPage(open_browser).click_button_by_phone()

    # Нажать на поле "Телефон"
    MainPage(open_browser).click_phone_field()

    # Ввести валидный номер телефона в поле "Телефон"
    MainPage(open_browser).enter_number_in_phone_field(phone=valid_phone_number_ui_python)

    # Нажать на поле ввода "Пароль"
    MainPage(open_browser).click_on_the_password_input_field()

    # Проверяем что Лейбл "Пароль" отображается над полем ввода пароля
    MainPage(open_browser).check_the_password_text_above_the_input_field()

    # Ввести валидный пароль
    MainPage(open_browser).enter_password_in_pass_field(password=valid_password)

    # Нажать на кнопку отображения пароля
    MainPage(open_browser).click_on_password_display_button()

    # Нажать на кнопку "Войти"
    MainPage(open_browser).click_button_login()
