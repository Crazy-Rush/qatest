import pytest

import allure
from test_framework.ui.data.user_data import valid_password, valid_phone_number_ui_python
from test_framework.ui.pages.main_pages.main_page import MainPage
from test_framework.ui.pages.profile_pages.cards_page import ProfileCardsPage
from test_framework.ui.pages.profile_pages.profile_main_page import ProfileMainPage


@pytest.mark.ui
@allure.id("C6025107")
@allure.title("C6025107. Просмотр имеющихся у клиента карт")
def test_ui_c6025107_view_existing_cards(open_browser):
    # Авторизация пользователя
    MainPage(open_browser).authorization(phone_number=valid_phone_number_ui_python, password=valid_password)

    # Переход в личный кабинет(профиль)
    MainPage(open_browser).click_logo_gor()

    # Открытие вкладки 'Карты'
    ProfileMainPage(open_browser).open_profile_cards_page()

    # Проверка отображения основных карт
    ProfileCardsPage(open_browser).check_displaying_basic_cards()

    # Клик на кнопку 'Раскрыть'
    ProfileCardsPage(open_browser).click_on_button_expand_hide()

    # Проверка отображения основных и дополнительных карт
    ProfileCardsPage(open_browser).check_displaying_additional_cards()
