import pytest

import allure
from test_framework.ui.data.user_data import valid_password, valid_phone_number_ui_python
from test_framework.ui.pages.main_pages.main_page import MainPage
from test_framework.ui.pages.personal_profile_pages.profile_settings_page import ProfileSettingsPage


@pytest.mark.ui
@allure.id("C6181482")
@allure.title("C6181482. Проверка изменения номера телефона с валидными данными цифры 0-9 .")
def test_ui_c6181482_success_change_phone_number_with_valid_data0_9(browser_change_phone_number_after_test):
    # Авторизация пользователя
    MainPage(browser_change_phone_number_after_test).authorization(
        phone_number=valid_phone_number_ui_python, password=valid_password
    )

    # Вход в личный кабинет
    MainPage(browser_change_phone_number_after_test).click_button_account()

    # Переход во вкладку "Настройки"
    ProfileSettingsPage(browser_change_phone_number_after_test).open_profile_options_page()
    MainPage(browser_change_phone_number_after_test).wait_logo_is_clickable()

    # Проверка активности кнопки Сохранить изменеия
    ProfileSettingsPage(browser_change_phone_number_after_test).check_button_save_changes_is_disable()

    # Нажать на иконку "карандаш"
    ProfileSettingsPage(browser_change_phone_number_after_test).click_on_button_change_phone_number()

    # Ввести новый цифру 1
    ProfileSettingsPage(browser_change_phone_number_after_test).enter_new_phone_number_to_phone_number_field("1")

    # Проверка совпадения введеного номера с номером в окне
    ProfileSettingsPage(browser_change_phone_number_after_test).check_user_phone_number_in_phone_number_field_equals(
        "+71xxxxxxxxx"
    )

    # Ввести новый цифры 234
    ProfileSettingsPage(
        browser_change_phone_number_after_test
    ).enter_new_phone_number_to_phone_number_field_with_no_clear("234")

    # Проверка совпадения введеного номера с номером в окне
    ProfileSettingsPage(browser_change_phone_number_after_test).check_user_phone_number_in_phone_number_field_equals(
        "+71234xxxxxx"
    )

    # Ввести новый цифры 567890
    ProfileSettingsPage(
        browser_change_phone_number_after_test
    ).enter_new_phone_number_to_phone_number_field_with_no_clear("567890")

    # Проверка совпадения введеного номера с номером в окне
    ProfileSettingsPage(browser_change_phone_number_after_test).check_user_phone_number_in_phone_number_field_equals(
        "+71234567890"
    )
