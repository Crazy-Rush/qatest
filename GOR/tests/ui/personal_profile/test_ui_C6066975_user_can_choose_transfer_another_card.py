import pytest

import allure
from test_framework.ui.data.user_data import valid_password, valid_phone_number_ui_python
from test_framework.ui.pages.main_pages.main_page import MainPage
from test_framework.ui.pages.profile_pages.profile_main_page import ProfileMainPage
from test_framework.ui.pages.profile_pages.transfer_via_cards_page import TransferCardsProfilePage


@pytest.mark.ui
@allure.id("C6066975")
@allure.title("C6066975. Пользователь может выбрать перевод на другую карту")
def test_ui_c6066975_user_can_choose_transfer_another_card(open_browser):
    # Авторизация пользователя
    MainPage(open_browser).authorization(phone_number=valid_phone_number_ui_python, password=valid_password)

    # Переход в личный кабинет(профиль)
    MainPage(open_browser).click_logo_gor()

    # Переход на страницу "Переводы"
    ProfileMainPage(open_browser).open_profile_transfer_via_cards_page()

    # В разделе "Переводы" выбрать таб "По карте"
    TransferCardsProfilePage(open_browser).click_button_by_card()

    # Проверка отображения формы для переводов по карте
    TransferCardsProfilePage(open_browser).check_displaying_elements_on_page("form_card_to_card_money_transfer_locator")
