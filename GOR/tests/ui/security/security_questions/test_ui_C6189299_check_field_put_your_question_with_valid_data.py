import pytest

import allure
from test_framework.ui.data.for_tests.data_c6189299 import data_for_security_question
from test_framework.ui.data.user_data import valid_password, valid_phone_number_ui_python
from test_framework.ui.pages.main_pages.main_page import MainPage
from test_framework.ui.pages.personal_profile_pages.profile_general_information_page import (
    ProfileGeneralInformationPage,
)
from test_framework.ui.pages.personal_profile_pages.profile_security_page import ProfileSecurityPage
from test_framework.ui.pages.profile_pages.profile_main_page import ProfileMainPage


@pytest.mark.ui
@pytest.mark.parametrize("expected_data", data_for_security_question)
@allure.id("C6189299")
@allure.title('C6189299. Валидные значения полей " Напишите ваш контрольный вопрос"')
def test_ui_C6189299_check_field_put_your_question_with_valid_data(open_browser, expected_data):
    # Авторизация пользователя
    MainPage(open_browser).authorization(phone_number=valid_phone_number_ui_python, password=valid_password)

    # Вход в личный кабинет
    ProfileMainPage(open_browser).open_profile_general_information_page()

    # Клик на вкладку "Безопасность"
    ProfileGeneralInformationPage(open_browser).open_profile_security_page()

    # Клик на кнопку "Смена контрольного вопроса"
    ProfileSecurityPage(open_browser).click_on_button_change_security_question()

    # Клик на "Написать свой вопрос" из выпадающего списка
    ProfileSecurityPage(open_browser).click_on_elements_on_drop_list("element_put_your_question_in_drop_list")

    # Ввод Твоего секретного вопроса и ответа
    ProfileSecurityPage(open_browser).enter_your_security_question(expected_data)
    ProfileSecurityPage(open_browser).enter_answer_for_your_security_question(expected_data)

    # Проверка введенного текста
    ProfileSecurityPage(open_browser).check_text_in_field("field_put_your_question", expected_data)
    ProfileSecurityPage(open_browser).check_text_in_field("field_put_your_answer", expected_data)
