import pytest

import allure
from test_framework.helpers.data_generation import get_custom_password_punctuation_only
from test_framework.ui.pages.main_pages.main_page import MainPage


@pytest.mark.ui
@allure.id("C5994512")
@allure.title("C5994512. Возможность ввода в поле ввода пароля спец.символов")
def test_ui_c5994512_enter_special_characters_in_password_field(open_browser):
    # Нажать на поле ввода пароля.
    MainPage(open_browser).click_on_the_password_input_field()

    # Ввести все возможные специальные символы, включая пробелы.
    MainPage(open_browser).enter_password_in_pass_field(password=get_custom_password_punctuation_only(10))

    # Проверка не отображания введеных букв и спец.символов в поле ввода номера паспорта
    MainPage(open_browser).check_no_entered_special_characters_in_password_field()
