import pytest

import allure
from test_framework.ui.data.user_data import valid_password, valid_phone_number_ui_python
from test_framework.ui.pages.main_pages.main_page import MainPage


@pytest.mark.ui
@allure.id("C6176275")
@allure.title("C6176275 Авторизация по номеру телефона и переход в личный кабинет")
def test_ui_c6176275_authorization_and_switch_to_personal_profile(open_browser):
    # Нажать на кнопку "по телефону"
    MainPage(open_browser).click_button_by_phone()

    # Нажать на поле "Телефон"
    MainPage(open_browser).click_phone_field()

    # Ввести валидный номер телефона в поле "Телефон"
    MainPage(open_browser).enter_number_in_phone_field(phone=valid_phone_number_ui_python)

    # Нажать на поле "Пароль"
    MainPage(open_browser).click_on_the_password_input_field()

    # Ввести валидный пароль
    MainPage(open_browser).enter_password_in_pass_field(password=valid_password)

    # Нажать на кнопку отображение пароля
    MainPage(open_browser).click_on_password_display_button()

    # Нажать на кнопку "Войти"
    MainPage(open_browser).click_button_login()

    # Нажать на кнопку "Аккаунт+имя"
    MainPage(open_browser).click_button_account()
