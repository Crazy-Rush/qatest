import pytest

import allure
from test_framework.ui.data.user_data import (
    invalid_data_for_change_password,
    valid_password,
    valid_phone_number_ui_python,
)
from test_framework.ui.pages.main_pages.main_page import MainPage
from test_framework.ui.pages.personal_profile_pages.profile_general_information_page import (
    ProfileGeneralInformationPage,
)
from test_framework.ui.pages.personal_profile_pages.profile_security_page import ProfileSecurityPage
from test_framework.ui.pages.profile_pages.profile_main_page import ProfileMainPage


@pytest.mark.ui
@pytest.mark.parametrize("expected_password", invalid_data_for_change_password)
@allure.id("C6176404")
@allure.title("C6176404. Невалидные значения полей 'Задайте новый пароль', 'Подтвердите новый пароль'")
def test_ui_C6176404_try_change_password_with_invalid_data(open_browser, expected_password):
    # Авторизация пользователя
    MainPage(open_browser).authorization(phone_number=valid_phone_number_ui_python, password=valid_password)

    # Вход в личный кабинет
    ProfileMainPage(open_browser).open_profile_general_information_page()

    # Клик на вкладку "Безопасность"
    ProfileGeneralInformationPage(open_browser).open_profile_security_page()

    # Клик на кнопку "Изменить пароль"
    ProfileSecurityPage(open_browser).click_on_button_change_password()

    # Ввод нового некорректного пароля
    ProfileSecurityPage(open_browser).enter_new_password(expected_password)

    # Клик на пусток поле
    ProfileSecurityPage(open_browser).click_field_current_password()

    # Проверка наличия сообщения об ошибке
    ProfileSecurityPage(open_browser).check_message_validation_password("text_validation_password_locator")

    # Ввод поддтверждения пароля
    ProfileSecurityPage(open_browser).enter_confirm_new_password(expected_password)

    # Клик на пусток поле
    ProfileSecurityPage(open_browser).click_field_current_password()

    # Проверка наличия сообщения об ошибке
    ProfileSecurityPage(open_browser).check_message_validation_password("text_message_missmatch_passwords_locator")
