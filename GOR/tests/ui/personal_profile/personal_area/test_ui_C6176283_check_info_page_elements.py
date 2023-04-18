import pytest

import allure
from test_framework.ui.data.user_data import valid_password, valid_phone_number_ui_python
from test_framework.ui.pages.main_pages.main_page import MainPage
from test_framework.ui.pages.personal_profile_pages.profile_general_information_page import (
    ProfileGeneralInformationPage,
)


@pytest.mark.ui
@allure.id("C6176283")
@allure.title("C6176283 Проверка отображения элементов в личном кабинете")
def test_ui_c6176283_check_info_page_elements_is_present(open_browser):
    # Авторизация пользователя
    MainPage(open_browser).authorization(phone_number=valid_phone_number_ui_python, password=valid_password)

    # Переход на страницу пользователя
    MainPage(open_browser).click_button_account()

    # Проверка наличия Лейбл "Фамилия" и поле с фамилией пользователя
    ProfileGeneralInformationPage(open_browser).check_displaying_elements_on_page("label_last_name_locator")
    ProfileGeneralInformationPage(open_browser).check_displaying_elements_on_page("field_last_name_locator")

    # Проверка наличия Лейбл "Имя" и поле с именем пользователя
    ProfileGeneralInformationPage(open_browser).check_displaying_elements_on_page("label_first_name_locator")
    ProfileGeneralInformationPage(open_browser).check_displaying_elements_on_page("field_first_name_locator")

    # Проверка наличия Лейбл "Отчество" и поле с отчеством пользователя
    ProfileGeneralInformationPage(open_browser).check_displaying_elements_on_page("label_past_name_locator")
    ProfileGeneralInformationPage(open_browser).check_displaying_elements_on_page("field_past_name_locator")

    # Проверка наличия Лейбл "Телефон" и поле с номером телефона пользователя
    ProfileGeneralInformationPage(open_browser).check_displaying_elements_on_page("label_telephone_locator")
    ProfileGeneralInformationPage(open_browser).check_displaying_elements_on_page("field_telephone_locator")

    # Проверка наличия Лейбл "Электронная почта" и поле для ввода данных
    ProfileGeneralInformationPage(open_browser).check_displaying_elements_on_page("label_email_locator")
    ProfileGeneralInformationPage(open_browser).check_displaying_elements_on_page("field_email_locator")

    # Проверка наличия Лейбл "Резиденство" и поле со статусом
    ProfileGeneralInformationPage(open_browser).check_displaying_elements_on_page("label_resident_locator")
    ProfileGeneralInformationPage(open_browser).check_displaying_elements_on_page("field_resident_locator")
