import pytest

import allure
from test_framework.ui.data.user_data import valid_password, valid_phone_number_ui_python
from test_framework.ui.pages.main_pages.main_page import MainPage
from test_framework.ui.pages.personal_profile_pages.profile_general_information_page import (
    ProfileGeneralInformationPage,
)
from test_framework.ui.pages.personal_profile_pages.profile_security_page import ProfileSecurityPage
from test_framework.ui.pages.profile_pages.profile_main_page import ProfileMainPage


@pytest.mark.ui
@allure.id("C6178842")
@allure.title(
    "C6178842. Валидные значения полей 'Введите текущий пароль', 'Задайте новый пароль', 'Подтвердите новый пароль'."
)
def test_ui_C6178842_check_fields_that_accepts_data(open_browser):
    # Авторизация пользователя
    MainPage(open_browser).authorization(phone_number=valid_phone_number_ui_python, password=valid_password)

    # Вход в личный кабинет
    ProfileMainPage(open_browser).open_profile_general_information_page()

    # Клик на вкладку "Безопасность"
    ProfileGeneralInformationPage(open_browser).open_profile_security_page()

    # Клик на кнопку "Изменить пароль"
    ProfileSecurityPage(open_browser).click_on_button_change_password()

    # Ввод одного символа во все поля
    ProfileSecurityPage(open_browser).enter_current_password("1")
    ProfileSecurityPage(open_browser).enter_new_password("1")
    ProfileSecurityPage(open_browser).enter_confirm_new_password("1")

    # Проверка полей, на несоответсвие введенному значению
    ProfileSecurityPage(open_browser).check_fields_value("field_current_password_locator", "1")
    ProfileSecurityPage(open_browser).check_fields_value("field_create_new_password_locator", "1")
    ProfileSecurityPage(open_browser).check_fields_value("field_confirm_new_password_locator", "1")

    # Ввод еще 2ух символов во все поля
    ProfileSecurityPage(open_browser).enter_current_password("Aa")
    ProfileSecurityPage(open_browser).enter_new_password("Aa")
    ProfileSecurityPage(open_browser).enter_confirm_new_password("Aa")

    # Проверка полей, на несоответсвие введенному значению
    ProfileSecurityPage(open_browser).check_fields_value("field_current_password_locator", "1Aa")
    ProfileSecurityPage(open_browser).check_fields_value("field_create_new_password_locator", "1Aa")
    ProfileSecurityPage(open_browser).check_fields_value("field_confirm_new_password_locator", "1Aa")

    # Ввод еще 3х спецсимволов во все поля
    ProfileSecurityPage(open_browser).enter_current_password("*!,")
    ProfileSecurityPage(open_browser).enter_new_password("*!,")
    ProfileSecurityPage(open_browser).enter_confirm_new_password("*!,")

    # Проверка полей, на несоответсвие введенному значению
    ProfileSecurityPage(open_browser).check_fields_value("field_current_password_locator", "1Aa*!,")
    ProfileSecurityPage(open_browser).check_fields_value("field_create_new_password_locator", "1Aa*!,")
    ProfileSecurityPage(open_browser).check_fields_value("field_confirm_new_password_locator", "1Aa*!,")
