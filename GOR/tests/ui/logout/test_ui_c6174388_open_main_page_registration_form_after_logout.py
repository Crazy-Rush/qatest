import pytest

import allure
from test_framework.ui.data.user_data import valid_password, valid_phone_number_ui_python
from test_framework.ui.pages.main_pages.main_page import MainPage
from test_framework.ui.pages.profile_pages.profile_main_page import ProfileMainPage


@pytest.mark.ui
@allure.id("C6174388")
@allure.title("C6174388 Проверка появления формы регистрации после выхода из профиля")
def test_ui_c6174388_open_main_page_registration_form_after_logout(open_browser):
    # Авторизация пользователя
    MainPage(open_browser).authorization(phone_number=valid_phone_number_ui_python, password=valid_password)

    # Выход пользователя
    ProfileMainPage(open_browser).click_button_logout()

    # Проверка появления формы регистрации
    MainPage(open_browser).check_main_page_after_reload()
