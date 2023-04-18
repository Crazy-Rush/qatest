import pytest

import allure
from test_framework.ui.data.for_tests.data_C6181468 import invalid_data_for_change_email as test_data
from test_framework.ui.data.user_data import valid_password, valid_phone_number_ui_python
from test_framework.ui.pages.main_pages.main_page import MainPage
from test_framework.ui.pages.personal_profile_pages.profile_settings_page import ProfileSettingsPage


@pytest.mark.skip(
    reason="На фронте временно отключили данный функционал из-за некорректной работы"
    " отображения сообщений об изменении поля"
)
@pytest.mark.ui
@pytest.mark.parametrize("expected_email", test_data)
@allure.id("C6181468")
@allure.title("C6181468. Проверка изменения email с невалидными данными.")
def test_ui_c6181468_check_email_change_with_invalid_data(open_browser, expected_email):
    # Авторизация пользователя
    MainPage(open_browser).authorization(phone_number=valid_phone_number_ui_python, password=valid_password)

    # Вход в личный кабинет
    MainPage(open_browser).click_button_account()

    # Переход во вкладку "Настройки"
    ProfileSettingsPage(open_browser).open_profile_options_page()
    MainPage(open_browser).wait_logo_is_clickable()

    # Нажать на кнопку "Карандаш" возле поля редактирования email
    ProfileSettingsPage(open_browser).click_on_button_change_email()

    # Проверка активности кнопки "Сохранить изменения"
    ProfileSettingsPage(open_browser).check_button_save_changes_is_disable()

    # Очистка поля и ввод в поле редактирования нового email
    ProfileSettingsPage(open_browser).enter_new_email_to_email_field(expected_email)

    # Клик на кнопку "Сохранить изменения"

    ProfileSettingsPage(open_browser).click_on_save_changes_button()
    """На фронте временно отключили данный функционал
           из-за некорректной работы отображения сообщений об изменении поля"""

    # проверка отсутствия сообщения о успешном изменении email
    ProfileSettingsPage(open_browser).check_not_displaying_elements_in_page("message_email_not_changed")
