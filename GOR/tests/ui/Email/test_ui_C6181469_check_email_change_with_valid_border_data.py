import pytest

import allure
from test_framework.ui.data.for_tests.data_c6181469_c6181470 import (
    valid_email_eleven,
    valid_email_plus_fourteen,
    valid_email_plus_ten,
)
from test_framework.ui.data.user_data import valid_password, valid_phone_number_ui_python
from test_framework.ui.pages.main_pages.main_page import MainPage
from test_framework.ui.pages.personal_profile_pages.profile_settings_page import ProfileSettingsPage


@pytest.mark.ui
@allure.id("c6181469")
@allure.title("c6181469. Проверка изменения email с валидными данными граничные значения.")
def test_ui_c6181469_check_email_change_with_valid_border_data(browser_change_email_after_test):
    # Авторизация пользователя
    MainPage(browser_change_email_after_test).authorization(
        phone_number=valid_phone_number_ui_python, password=valid_password
    )

    # Вход в личный кабинет
    MainPage(browser_change_email_after_test).click_button_account()

    # Переход во вкладку "Настройки"
    ProfileSettingsPage(browser_change_email_after_test).open_profile_options_page()
    MainPage(browser_change_email_after_test).wait_logo_is_clickable()

    # Нажать на иконку "карандаш"
    ProfileSettingsPage(browser_change_email_after_test).click_on_button_change_email()

    # Отредактировать существующий email валидными данными.
    ProfileSettingsPage(browser_change_email_after_test).enter_new_email_to_email_field(valid_email_eleven)

    # Проверка активности кнопки "Сохранить изменения"
    ProfileSettingsPage(browser_change_email_after_test).check_button_save_changes_is_disable()

    # Нажать на иконку "карандаш"
    ProfileSettingsPage(browser_change_email_after_test).click_on_button_change_email()

    # Отредактировать существующий email невалидными данными.
    ProfileSettingsPage(browser_change_email_after_test).enter_new_email_to_email_field(valid_email_plus_ten)

    # Проверка активности кнопки "Сохранить изменения"
    ProfileSettingsPage(browser_change_email_after_test).check_button_save_changes_is_disable()

    # Нажать на иконку "карандаш"
    ProfileSettingsPage(browser_change_email_after_test).click_on_button_change_email()

    # Отредактировать существующий email невалидными данными.
    ProfileSettingsPage(browser_change_email_after_test).enter_new_email_to_email_field(valid_email_plus_fourteen)

    # Проверка активности кнопки "Сохранить изменения"
    ProfileSettingsPage(browser_change_email_after_test).check_button_save_changes_is_disable()
