import pytest

import allure
from test_framework.ui.data.user_data import valid_password, valid_phone_number_ui_python
from test_framework.ui.pages.main_pages.main_page import MainPage
from test_framework.ui.pages.profile_pages.profile_main_page import ProfileMainPage


@pytest.mark.ui
@allure.id("C6174395")
@allure.title("C6174395 Проверка отображения на главной странице элементов популярных услуг")
def test_ui_c6174395_popular_services_for_elements_is_displayed(open_browser):
    # Авторизация пользователя
    MainPage(open_browser).authorization(phone_number=valid_phone_number_ui_python, password=valid_password)

    # Проверка наличия иконки услуги Оплаты связи
    ProfileMainPage(open_browser).check_displaying_elements_on_page("popular_services_phone_pay_locator")

    # Проверка наличия названия услуги Оплаты связи
    ProfileMainPage(open_browser).check_displaying_elements_on_page("popular_services_phone_pay_label_locator")

    # Проверка наличия иконки услуги Перевод на карту
    ProfileMainPage(open_browser).check_displaying_elements_on_page("popular_services_money_transfer_locator")

    # Проверка наличия названия услуги Перевод на карту
    ProfileMainPage(open_browser).check_displaying_elements_on_page("popular_services_money_transfer_label_locator")

    # Проверка наличия иконки услуги Утилиты
    ProfileMainPage(open_browser).check_displaying_elements_on_page("popular_services_utilities_locator")

    # Проверка наличия названия услуги Утилиты
    ProfileMainPage(open_browser).check_displaying_elements_on_page("popular_services_utilities_label_locator")

    # Проверка наличия иконки услуги Обмен валюты
    ProfileMainPage(open_browser).check_displaying_elements_on_page("popular_services_exchange_locator")

    # Проверка наличия названия услуги Обмен валюты
    ProfileMainPage(open_browser).check_displaying_elements_on_page("popular_services_exchange_label_locator")

    # Проверка наличия иконки Добавить
    ProfileMainPage(open_browser).check_displaying_elements_on_page("popular_services_add_new_service_locator")

    # Проверка наличия названия иконки Добавить
    ProfileMainPage(open_browser).check_displaying_elements_on_page("popular_services_add_new_service_label_locator")
