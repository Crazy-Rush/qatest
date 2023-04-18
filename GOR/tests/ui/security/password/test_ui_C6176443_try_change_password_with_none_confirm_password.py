import pytest

import allure
from test_framework.ui.data.user_data import password, valid_password, valid_phone_number_ui_python
from test_framework.ui.pages.main_pages.main_page import MainPage
from test_framework.ui.pages.personal_profile_pages.profile_general_information_page import (
    ProfileGeneralInformationPage,
)
from test_framework.ui.pages.personal_profile_pages.profile_security_page import ProfileSecurityPage
from test_framework.ui.pages.profile_pages.profile_main_page import ProfileMainPage


@pytest.mark.ui
@allure.id("C6176443")
@allure.title("C6176443. Изменить пароль в личном кабинете, заполнив несколько полей формы.")
def test_ui_C6176443_try_change_password_with_none_confirm_password(open_browser):
    # Авторизация пользователя
    MainPage(open_browser).authorization(phone_number=valid_phone_number_ui_python, password=valid_password)

    # Вход в личный кабинет
    ProfileMainPage(open_browser).open_profile_general_information_page()

    # Клик на вкладку "Безопасность"
    ProfileGeneralInformationPage(open_browser).open_profile_security_page()

    # Клик на кнопку "Изменить пароль"
    ProfileSecurityPage(open_browser).click_on_button_change_password()

    # Ввод текущего пароля
    ProfileSecurityPage(open_browser).enter_current_password(valid_password)

    # Ввод нового пароля
    ProfileSecurityPage(open_browser).enter_new_password(password)

    # Проверка, что кнопка подтвердить не активна
    ProfileSecurityPage(open_browser).check_no_active_submit_button()
