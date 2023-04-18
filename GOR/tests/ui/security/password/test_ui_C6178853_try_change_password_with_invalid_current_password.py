import pytest

import allure
from test_framework.ui.data.user_data import (
    password,
    valid_password,
    valid_password_autofirstnametest,
    valid_phone_number_ui_python,
)
from test_framework.ui.pages.main_pages.main_page import MainPage
from test_framework.ui.pages.personal_profile_pages.profile_general_information_page import (
    ProfileGeneralInformationPage,
)
from test_framework.ui.pages.personal_profile_pages.profile_security_page import ProfileSecurityPage
from test_framework.ui.pages.profile_pages.profile_main_page import ProfileMainPage


@pytest.mark.ui
@allure.id("C6178853")
@allure.title(
    "C6178853. "
    "Изменение пароля: данные поля 'Подтвердите новый пароль' не совпадают с данными поля 'Задайте новый пароль'."
)
def test_ui_C6178853_try_change_password_with_invalid_current_password(open_browser):
    # Авторизация пользователя
    MainPage(open_browser).authorization(phone_number=valid_phone_number_ui_python, password=valid_password)

    # Вход в личный кабинет
    ProfileMainPage(open_browser).open_profile_general_information_page()

    # Клик на вкладку "Безопасность"
    ProfileGeneralInformationPage(open_browser).open_profile_security_page()

    # Клик на кнопку "Изменить пароль"
    ProfileSecurityPage(open_browser).click_on_button_change_password()

    # Ввод одного символа во все поля
    ProfileSecurityPage(open_browser).enter_current_password(valid_password_autofirstnametest)
    ProfileSecurityPage(open_browser).enter_new_password(password)
    ProfileSecurityPage(open_browser).enter_confirm_new_password(password)

    # Клик на пусток поле
    ProfileSecurityPage(open_browser).click_submit_button()

    # Проверка появления сообщения "Пароли не совподают"
    ProfileSecurityPage(open_browser).check_message_password_not_change()
