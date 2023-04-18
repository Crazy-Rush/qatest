import pytest

import allure
from test_framework.ui.data.user_data import valid_password, valid_phone_number_ui_python
from test_framework.ui.pages.main_pages.main_page import MainPage
from test_framework.ui.pages.personal_profile_pages.profile_general_information_page import (
    ProfileGeneralInformationPage,
)
from test_framework.ui.pages.personal_profile_pages.profile_notifications_page import ProfileNotificationPage


@pytest.mark.ui
@allure.id("C6181462")
@allure.title("C6181462 Проверка переключения switcher-ов на ON")
def test_ui_c6181462_check_switch_notifications_to_off(open_browser):
    # Авторизация пользователя
    MainPage(open_browser).authorization(phone_number=valid_phone_number_ui_python, password=valid_password)

    # Переход в личный кабинет
    MainPage(open_browser).click_button_account()

    # Переход во вкладку "Настройки"
    ProfileNotificationPage(open_browser).open_profile_options_page()
    MainPage(open_browser).wait_logo_is_clickable()

    # Переключить чекбокс Email Рассылка на ON
    ProfileNotificationPage(open_browser).click_checkbox_notification(
        "checkbox_email_notification_locator", "label_email_notification_locator", "ON"
    )

    # Проверка переключение чекбокса Email на ON
    ProfileNotificationPage(open_browser).check_notification_checkbox_switch("label_email_notification_locator", "ON")

    # Переключить чекбокс SMS Рассылка на ON
    ProfileNotificationPage(open_browser).click_checkbox_notification(
        "checkbox_sms_notification_locator", "label_sms_notification_locator", "ON"
    )

    # Проверка переключение чекбокса SMS на ON
    ProfileNotificationPage(open_browser).check_notification_checkbox_switch("label_sms_notification_locator", "ON")

    # Переключить чекбокс Push Рассылка на ON
    ProfileNotificationPage(open_browser).click_checkbox_notification(
        "checkbox_push_notification_locator", "label_push_notification_locator", "ON"
    )

    # Проверка переключение чекбокса Push на ON
    ProfileNotificationPage(open_browser).check_notification_checkbox_switch("label_push_notification_locator", "ON")

    # Переместиться на вкладку Безопасность
    ProfileGeneralInformationPage(open_browser).open_profile_security_page()

    # Переместиться на вкладку Настройки
    ProfileNotificationPage(open_browser).open_profile_options_page()

    # Убедиться что переключатели на ON
    ProfileNotificationPage(open_browser).check_notification_checkbox_switch("label_email_notification_locator", "ON")
    ProfileNotificationPage(open_browser).check_notification_checkbox_switch("label_sms_notification_locator", "ON")
    ProfileNotificationPage(open_browser).check_notification_checkbox_switch("label_push_notification_locator", "ON")
