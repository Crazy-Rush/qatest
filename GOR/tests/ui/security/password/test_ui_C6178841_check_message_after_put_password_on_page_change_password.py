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
@allure.id("C6178841")
@allure.title(
    "C6178841. "
    "Невалидные граничные значения полей 'Введите текущий пароль', 'Задайте новый пароль', 'Подтвердите новый пароль'."
)
def test_ui_C6178841_check_message_after_put_password_on_page_change_password(open_browser):
    # Авторизация пользователя
    MainPage(open_browser).authorization(phone_number=valid_phone_number_ui_python, password=valid_password)

    # Вход в личный кабинет
    ProfileMainPage(open_browser).open_profile_general_information_page()

    # Клик на вкладку "Безопасность"
    ProfileGeneralInformationPage(open_browser).open_profile_security_page()

    # Клик на кнопку "Изменить пароль"
    ProfileSecurityPage(open_browser).click_on_button_change_password()

    # Проверка с 5 символами
    # Ввод пароля и проверка сообщения в поле Введите текущий пароль
    ProfileSecurityPage(open_browser).enter_current_password("Aa123")
    ProfileSecurityPage(open_browser).click_field_new_password()
    ProfileSecurityPage(open_browser).check_message_validation_password("text_validation_password_locator")

    # Ввод пароля и проверка сообщения в поле Введите новый пароль
    ProfileSecurityPage(open_browser).enter_new_password("Aa123")
    ProfileSecurityPage(open_browser).click_field_current_password()
    ProfileSecurityPage(open_browser).check_message_validation_password(
        "text_validation_password_locator_under_new_password"
    )

    # Ввод пароля и проверка сообщения в поле Подтвердите введенный пароль
    ProfileSecurityPage(open_browser).enter_confirm_new_password("Aa123")
    ProfileSecurityPage(open_browser).click_field_current_password()
    ProfileSecurityPage(open_browser).check_message_validation_password("text_message_missmatch_passwords_locator")

    # Клик на кнопку "Отменить"
    ProfileSecurityPage(open_browser).click_button_cancel_data_on_page_change_password()

    # Проверка с 21 символами
    # Ввод паролей
    ProfileSecurityPage(open_browser).enter_current_password("12As4jasRt12345)/asd1")
    ProfileSecurityPage(open_browser).enter_new_password("12As4jasRt12345)/asd1")
    ProfileSecurityPage(open_browser).enter_confirm_new_password("12As4jasRt12345)/asd1")

    # Проверка полей, на несоответсвие введенному значению
    ProfileSecurityPage(open_browser).check_fields_on_page_change_password_not_equals(
        "field_current_password_locator", "12As4jasRt12345)/asd1"
    )
    ProfileSecurityPage(open_browser).check_fields_on_page_change_password_not_equals(
        "field_create_new_password_locator", "12As4jasRt12345)/asd1"
    )
    ProfileSecurityPage(open_browser).check_fields_on_page_change_password_not_equals(
        "field_confirm_new_password_locator", "12As4jasRt12345)/asd1"
    )
