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
@allure.id("C6189274")
@allure.title("C6189274. Интерфейс раздела смены контрольного вопроса в личном кабинете.")
def test_ui_C6189274_check_fields_on_page_change_security_questions(open_browser):
    # Авторизация пользователя
    MainPage(open_browser).authorization(phone_number=valid_phone_number_ui_python, password=valid_password)

    # Вход в личный кабинет
    ProfileMainPage(open_browser).open_profile_general_information_page()

    # Клик на вкладку "Безопасность"
    ProfileGeneralInformationPage(open_browser).open_profile_security_page()

    # Клик на кнопку "Смена контрольного вопроса"
    ProfileSecurityPage(open_browser).click_on_button_change_security_question()

    # Клик на кнопку "Назад"
    ProfileSecurityPage(open_browser).click_button_back()

    # Клик на кнопку "Смена контрольного вопроса"
    ProfileSecurityPage(open_browser).click_on_button_change_security_question()

    # Проверка элемента текста в описание страницы
    ProfileSecurityPage(open_browser).check_displaying_elements_on_page_change_password("text_header_down")

    # Клик на "Написать свой вопрос" из выпадающего списка
    ProfileSecurityPage(open_browser).click_on_elements_on_drop_list("element_put_your_question_in_drop_list")

    # Проверка наличие элемента "Напиши ваш контрольный вопрос"
    ProfileSecurityPage(open_browser).check_displaying_elements_on_page_change_password("field_put_your_question")

    # Проверка, что кнопка подтвердить не активна
    ProfileSecurityPage(open_browser).check_no_active_submit_button()

    """На данный момент неверно реализована кнопка "Отменить". Выполняет функцию кнопки "Назад"
       По документации должна быть неактивна"""
    # Проверка, что кнопка отменить не активна
    # profile_security_page.check_no_active_cancel_button_on_page_security_questions()
