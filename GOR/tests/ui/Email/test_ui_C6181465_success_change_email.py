import pytest

import allure
from test_framework.helpers.data_generation import get_custom_email
from test_framework.ui.data.user_data import valid_email_ui_python, valid_password, valid_phone_number_ui_python
from test_framework.ui.pages.main_pages.main_page import MainPage
from test_framework.ui.pages.personal_profile_pages.profile_settings_page import ProfileSettingsPage


@pytest.mark.skip(
    reason="На фронте временно отключили данный функционал из-за некорректной работы отображения"
    "сообщений об изменении поля"
)
@pytest.mark.ui
@allure.id("C6181465")
@allure.title("C6181465. Успешное изменение Email в личном кабинете.")
def test_ui_c6181465_success_change_email(browser_change_email_after_test):
    # Получение рандомного email
    random_email = get_custom_email()

    # Авторизация пользователя
    MainPage(browser_change_email_after_test).authorization(
        phone_number=valid_phone_number_ui_python, password=valid_password
    )
    # Вход в личный кабинет
    MainPage(browser_change_email_after_test).click_button_account()

    # Переход во вкладку "Настройки"
    ProfileSettingsPage(browser_change_email_after_test).open_profile_options_page()
    MainPage(browser_change_email_after_test).wait_logo_is_clickable()

    # Проверка совпадения email
    ProfileSettingsPage(browser_change_email_after_test).check_user_email_in_email_field_equals(
        expected_email=valid_email_ui_python
    )

    # Нажать на иконку "карандаш"
    ProfileSettingsPage(browser_change_email_after_test).click_on_button_change_email()

    # Проверка активности кнопки "Сохранить изменения"
    ProfileSettingsPage(browser_change_email_after_test).check_button_save_changes_is_disable()

    # Отредактировать существующий email валидными данными.
    ProfileSettingsPage(browser_change_email_after_test).enter_new_email_to_email_field(random_email)

    # Проверка активности кнопки "Сохранить изменения"
    ProfileSettingsPage(browser_change_email_after_test).check_button_save_changes_is_disable()

    # Нажать на кнопку "Сохранить изменения".

    ProfileSettingsPage(browser_change_email_after_test).click_on_save_changes_button()
    """На фронте временно отключили данный функционал
       из-за некорректной работы отображения сообщений об изменении поля"""

    # Проверка появления статуса "Адрес подтверждён".
    ProfileSettingsPage(browser_change_email_after_test).check_message_success_change_email()
