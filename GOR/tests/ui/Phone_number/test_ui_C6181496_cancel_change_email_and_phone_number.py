import pytest

import allure
from test_framework.ui.data.for_tests.data_C6181467_C6181496 import new_phone_number, valid_email
from test_framework.ui.data.user_data import valid_email_ui_python, valid_password, valid_phone_number_ui_python
from test_framework.ui.pages.main_pages.main_page import MainPage
from test_framework.ui.pages.personal_profile_pages.profile_settings_page import ProfileSettingsPage


@pytest.mark.ui
@allure.id("C6181496")
@allure.title("C6181496. Отмена изменений в поле email и Номер телефона.")
def test_ui_c6181496_cancel_change_email_and_phone_number(open_browser):
    # Авторизация пользователя
    MainPage(open_browser).authorization(phone_number=valid_phone_number_ui_python, password=valid_password)

    # Вход в личный кабинет
    MainPage(open_browser).click_button_account()

    # Переход во вкладку "Настройки"
    ProfileSettingsPage(open_browser).open_profile_options_page()
    MainPage(open_browser).wait_logo_is_clickable()

    # Нажать на иконку "карандаш"
    ProfileSettingsPage(open_browser).click_on_button_change_email()

    # Отредактировать существующий email валидными данными.
    ProfileSettingsPage(open_browser).enter_new_email_to_email_field(valid_email)

    # Нажать на кнопку сбросить изменения
    ProfileSettingsPage(open_browser).click_on_dismiss_changes_button()

    # Проверка отмены изменений в поле Email
    ProfileSettingsPage(open_browser).check_user_email_in_email_field_equals(valid_email_ui_python)

    # Нажать на иконку "карандаш"
    ProfileSettingsPage(open_browser).click_on_button_change_phone_number()

    # Отредактировать существующий номер телефона валидными данными.
    ProfileSettingsPage(open_browser).enter_new_phone_number_to_phone_number_field(new_phone_number)

    # Нажать на кнопку сбросить изменения
    ProfileSettingsPage(open_browser).click_on_dismiss_changes_button()

    # Проверка отмены изменений в поле Номер телефона
    ProfileSettingsPage(open_browser).check_user_phone_number_in_phone_number_field_equals(
        "+7" + valid_phone_number_ui_python
    )
