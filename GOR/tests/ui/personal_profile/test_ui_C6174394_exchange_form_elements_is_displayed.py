import pytest

import allure
from test_framework.ui.data.user_data import valid_password, valid_phone_number_ui_python
from test_framework.ui.pages.main_pages.main_page import MainPage
from test_framework.ui.pages.profile_pages.profile_main_page import ProfileMainPage


@pytest.mark.ui
@allure.id("C6174394")
@allure.title("C6174394 Проверка отображения на главной странице элементов курсов валют")
def test_ui_c6174394_check_exchange_form_elements_is_present(open_browser):
    # Авторизация пользователя
    MainPage(open_browser).authorization(phone_number=valid_phone_number_ui_python, password=valid_password)

    # Проверка наличия названия столбца "Валюта"
    ProfileMainPage(open_browser).check_displaying_elements_on_page("exchange_table_currency_column_name")

    # Проверка наличия названия столбца "Покупка"
    ProfileMainPage(open_browser).check_displaying_elements_on_page("exchange_table_purchase_column_name")

    # Проверка наличия названия столбца "Продажа"
    ProfileMainPage(open_browser).check_displaying_elements_on_page("exchange_table_sale_column_name")

    # Проверка наличия флага страны
    ProfileMainPage(open_browser).check_displaying_elements_on_page("exchange_table_flag_image")

    # Проверка наличия кода страны
    ProfileMainPage(open_browser).check_displaying_elements_on_page("exchange_table_country_code")

    # Проверка наличия названия страны
    ProfileMainPage(open_browser).check_displaying_elements_on_page("exchange_table_currency_country_name")

    # Проверка наличия курса покупки валюты
    ProfileMainPage(open_browser).check_displaying_elements_on_page("exchange_table_bye_currency")

    # Проверка наличия курса продажи валюты
    ProfileMainPage(open_browser).check_displaying_elements_on_page("exchange_table_sell_currency")
