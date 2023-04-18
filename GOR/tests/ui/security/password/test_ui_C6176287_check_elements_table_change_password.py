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
@allure.id("C6176287")
@allure.title("C6176287. Интерфейс раздела 'Изменить пароль' в табе 'Безопасность' личного кабинета.")
def test_ui_C6176287_check_elements_table_change_password(open_browser):
    # Авторизация пользователя
    MainPage(open_browser).authorization(phone_number=valid_phone_number_ui_python, password=valid_password)

    # Вход в личный кабинет
    ProfileMainPage(open_browser).open_profile_general_information_page()

    # Клик на вкладку "Безопасность"
    ProfileGeneralInformationPage(open_browser).open_profile_security_page()

    # Клик на кнопку "Изменить пароль"
    ProfileSecurityPage(open_browser).click_on_button_change_password()

    # Проверка наличия элемента кнопки "Назад"
    ProfileSecurityPage(open_browser).check_displaying_elements_on_page_change_password("button_back")
    # Проверка наличия заголовка
    ProfileSecurityPage(open_browser).check_displaying_elements_on_page_change_password("text_header")
    # Проверка наличия надписи под заголовком
    ProfileSecurityPage(open_browser).check_displaying_elements_on_page_change_password("text_header_down")
    # Проверка наличия поля "Введите текущий пароль"
    ProfileSecurityPage(open_browser).check_displaying_elements_on_page_change_password(
        "field_current_password_locator"
    )
    # Проверка наличия поля "Введите новый пароль"
    ProfileSecurityPage(open_browser).check_displaying_elements_on_page_change_password(
        "field_create_new_password_locator"
    )
    # Проверка наличия поля "Подтвердите новый пароль"
    ProfileSecurityPage(open_browser).check_displaying_elements_on_page_change_password(
        "field_confirm_new_password_locator"
    )
    # Проверка наличия элемента кнопки "Подтвердить"
    ProfileSecurityPage(open_browser).check_displaying_elements_on_page_change_password("button_confirm")
    # Проверка наличия элемента кнопки "Отмена"
    ProfileSecurityPage(open_browser).check_displaying_elements_on_page_change_password("button_cancel")
