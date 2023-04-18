import pytest

import allure
from test_framework.ui.data.for_tests.data_c5994510 import four_digit, one_digit
from test_framework.ui.data.user_data import valid_password
from test_framework.ui.pages.main_pages.main_page import MainPage


@pytest.mark.ui
@allure.id("C5994510")
@allure.title("C5994510. Проверка граничных значений поля ввода номера телефона")
def test_ui_c5994510_check_boundary_values_field_phone_number(open_browser):
    # Нажать на кнопку "По телефону"
    MainPage(open_browser).click_button_by_phone()

    # Ввести валидный пароль в поле ввода пароля
    MainPage(open_browser).enter_password_in_pass_field(password=valid_password)

    # Кнопка "Войти" неактивна
    MainPage(open_browser).check_status_button_login_disabled()

    # Нажать на поле ввода номера телефона
    MainPage(open_browser).click_phone_field()

    # Ввести 1 цифру
    MainPage(open_browser).enter_number_in_phone_field(phone=one_digit)

    # Кнопка "Войти" неактивна
    MainPage(open_browser).check_status_button_login_disabled()

    # Ввести 4 цифры
    MainPage(open_browser).enter_number_in_phone_field(phone=four_digit)

    # Кнопка "Войти" неактивна
    MainPage(open_browser).check_status_button_login_disabled()

    # Ввести 4 цифры
    MainPage(open_browser).enter_number_in_phone_field(phone=four_digit)

    # Кнопка "Войти" неактивна
    MainPage(open_browser).check_status_button_login_disabled()

    # Ввести 1 цифру
    MainPage(open_browser).enter_number_in_phone_field(phone=one_digit)

    # Проверка активности кнопки "Войти"
    MainPage(open_browser).check_active_button_login()

    # Ввести 1 цифру
    MainPage(open_browser).enter_number_in_phone_field(phone=one_digit)

    # Проверка не отображания последней введенной цифры
    MainPage(open_browser).check_entered_digits_phone_field()

    # Нажать на кнопку "Войти"
    MainPage(open_browser).click_button_login()
