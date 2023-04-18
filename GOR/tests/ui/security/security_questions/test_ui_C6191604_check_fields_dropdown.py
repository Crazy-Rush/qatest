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
@allure.id("C6191604")
@allure.title("C6191604. Содержимое дропдауна смены контрольного вопроса и его функциональность.")
def test_ui_C6191604_check_fields_dropdown(open_browser):
    # Авторизация пользователя
    MainPage(open_browser).authorization(phone_number=valid_phone_number_ui_python, password=valid_password)

    # Вход в личный кабинет
    ProfileMainPage(open_browser).open_profile_general_information_page()

    # Клик на вкладку "Безопасность"
    ProfileGeneralInformationPage(open_browser).open_profile_security_page()

    # Клик на кнопку "Смена контрольного вопроса"
    ProfileSecurityPage(open_browser).click_on_button_change_security_question()

    # Клик на кнопку выпадения дроплиста
    ProfileSecurityPage(open_browser).click_on_button_drop_list()

    # Проверка, что элемент  дроплиста "Напишите свой вопрос" присутствуют на странице
    ProfileSecurityPage(open_browser).check_displaying_elements_on_page_change_password(
        "element_put_your_question_in_drop_list"
    )
    # Проверка, что элемент  дроплиста "Девичья фамилия матери" присутствуют на странице
    ProfileSecurityPage(open_browser).check_displaying_elements_on_page_change_password(
        "element_lastname_your_mother_in_drop_list"
    )
    # Проверка, что элемент  дроплиста "Имя лучшего друга" присутствуют на странице
    ProfileSecurityPage(open_browser).check_displaying_elements_on_page_change_password(
        "element_name_your_close_friend"
    )
    # Проверка, что элемент  дроплиста "Любимая книга" присутствуют на странице
    ProfileSecurityPage(open_browser).check_displaying_elements_on_page_change_password("element_your_favorite_book")
    # Проверка, что элемент  дроплиста "Любимый цвет" присутствуют на странице
    ProfileSecurityPage(open_browser).check_displaying_elements_on_page_change_password("element_your_favorite_color")
    # Проверка, что элемент  дроплиста "Любимое блюдо" присутствуют на странице
    ProfileSecurityPage(open_browser).check_displaying_elements_on_page_change_password("element_your_favorite_dish")
