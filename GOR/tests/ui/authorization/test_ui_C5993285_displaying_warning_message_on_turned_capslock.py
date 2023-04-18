import pytest

import allure
from test_framework.ui.pages.main_pages.main_page import MainPage


@pytest.mark.ui
@allure.id("C5993285")
@allure.title("C5993285. Появление предупреждающего сообщения о включенном CapsLock при вводе пароля")
def test_ui_c5993285_displaying_warning_message_on_turned_capslock(open_browser):
    # Нажать на поле ввода "Пароль"
    MainPage(open_browser).click_on_the_password_input_field()

    # Нажатие клавиши CapsLock
    MainPage(open_browser).turn_on_capslock()

    # Проверка появления сообщения "Включен CapsLock"
    MainPage(open_browser).check_message_about_on_turned_capslock()

    # Нажатие клавиши CapsLock
    MainPage(open_browser).turn_on_capslock()

    # Проверка не отображения сообщения "Включен CapsLock"
    MainPage(open_browser).check_no_message_about_on_turned_capslock()
