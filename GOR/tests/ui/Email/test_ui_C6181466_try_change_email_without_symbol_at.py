import pytest

import allure
from test_framework.ui.data.user_data import valid_password, valid_phone_number_ui_python
from test_framework.ui.pages.main_pages.main_page import MainPage
from test_framework.ui.pages.personal_profile_pages.profile_settings_page import ProfileSettingsPage
from test_framework.ui.pages.profile_pages.profile_main_page import ProfileMainPage


@pytest.mark.skip(
    reason="На фронте временно отключили данный функционал из-за некорректной работы отображения"
    "сообщений об изменении поля"
)
@pytest.mark.ui
@allure.id("C6178891")
@allure.title("C6178891. Проверка статуса 'Адрес не подтвержден' при редактировании email..")
def test_C6181466_try_change_email_without_symbol_at(open_browser):
    # Переменная без символа "@"
    email_without_at = "asdr1289mail.ru"

    # Авторизация пользователя
    MainPage(open_browser).authorization(phone_number=valid_phone_number_ui_python, password=valid_password)

    # Вход в личный кабинет
    ProfileMainPage(open_browser).open_profile_general_information_page()

    # Вход во вкладку настройки
    ProfileSettingsPage(open_browser).open_profile_options_page()

    # Клик на кнопку "Карандаш"
    ProfileSettingsPage(open_browser).click_on_button_change_email()

    # Очистка поля Еmail и ввод нового Email
    ProfileSettingsPage(open_browser).enter_new_email_to_email_field(email_without_at)

    # Сохраняем изменения
    ProfileSettingsPage(open_browser).click_on_save_changes_button()

    # Проверка сообщения об ошибке
    ProfileSettingsPage(open_browser).check_message_not_change_email()
