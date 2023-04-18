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
@allure.id("C6179836")
@allure.title("C6179836. Появление дополнительного поля ввода при выборе дропдауна 'Написать свой вопрос'")
def test_ui_C6179836_check_appearance_new_fields_on_page_change_security_question(open_browser):
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

    # Проверка наличие элемента "Напиши ваш контрольный вопрос"
    ProfileSecurityPage(open_browser).check_displaying_elements_on_page_change_password("field_put_your_question")
