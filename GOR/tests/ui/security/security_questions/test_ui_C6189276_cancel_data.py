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
@allure.id("C6189276")
@allure.title('C6189276. Исчезновение дополнительного поля "Напишите ваш контрольный вопрос"')
def test_ui_C6189276_cancel_data(open_browser):
    # Авторизация пользователя
    MainPage(open_browser).authorization(phone_number=valid_phone_number_ui_python, password=valid_password)

    # Вход в личный кабинет
    ProfileMainPage(open_browser).open_profile_general_information_page()

    # Клик на вкладку "Безопасность"
    ProfileGeneralInformationPage(open_browser).open_profile_security_page()

    # Клик на кнопку "Смена контрольного вопроса"
    ProfileSecurityPage(open_browser).click_on_button_change_security_question()

    # Клик на "Девичья фамилия матери"
    ProfileSecurityPage(open_browser).click_on_elements_on_drop_list("element_lastname_your_mother_in_drop_list")

    # Проверка, что в поле выбора появился текст "Девичья фамилия матери"
    ProfileSecurityPage(open_browser).check_fields_value("field_choose_your_question", "Девичья фамилия матери")

    # Ввод значений в поле ответ на секретный вопрос
    ProfileSecurityPage(open_browser).enter_answer_for_your_security_question("asdqwedsasa")

    # Очистка поля
    ProfileSecurityPage(open_browser).click_button_cancel_data_on_page_change_security_question()
