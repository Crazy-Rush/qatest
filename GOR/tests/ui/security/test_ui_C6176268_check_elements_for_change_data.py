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
@allure.id("C6176268")
@allure.title("C6176268. Интерфейс таба 'Безопасность'' и его составляющие элементы.")
def test_ui_C6176268_check_elements_for_change_data(open_browser):
    # Авторизация пользователя
    MainPage(open_browser).authorization(phone_number=valid_phone_number_ui_python, password=valid_password)

    # Вход в личный кабинет
    ProfileMainPage(open_browser).open_profile_general_information_page()

    # Клик на вкладку "Безопасность"
    ProfileGeneralInformationPage(open_browser).open_profile_security_page()

    # Ожидание что элементы "Изменить пароль" и "Изменить контрольный вопрос" присутствуют на странице
    ProfileSecurityPage(open_browser).check_displaying_button_change_password()
    ProfileSecurityPage(open_browser).check_displaying_button_change_secret_question()
