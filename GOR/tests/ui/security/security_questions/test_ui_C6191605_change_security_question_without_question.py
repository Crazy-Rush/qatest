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
@allure.id("C6191605")
@allure.title("C6191605. Изменить контрольный вопрос,не выбрав вопрос")
def test_ui_C6191605_change_security_question_without_question(open_browser):
    # Авторизация пользователя
    MainPage(open_browser).authorization(phone_number=valid_phone_number_ui_python, password=valid_password)

    # Вход в личный кабинет
    ProfileMainPage(open_browser).open_profile_general_information_page()

    # Клик на вкладку "Безопасность"
    ProfileGeneralInformationPage(open_browser).open_profile_security_page()

    # Клик на кнопку "Смена контрольного вопроса"
    ProfileSecurityPage(open_browser).click_on_button_change_security_question()

    # Заполнить поле введите ответ на секретный вопрос
    ProfileSecurityPage(open_browser).enter_answer_for_your_security_question("Asdfsd1234A")

    # Проверка, что кнопка подтвердить неактивна
    ProfileSecurityPage(open_browser).check_no_active_submit_button()
