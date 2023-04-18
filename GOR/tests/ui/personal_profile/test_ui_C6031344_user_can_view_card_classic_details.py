import pytest

import allure
from test_framework.ui.data.user_data import valid_password, valid_phone_number_ui_python
from test_framework.ui.pages.main_pages.main_page import MainPage
from test_framework.ui.pages.profile_pages.cards_page import ProfileCardsPage
from test_framework.ui.pages.profile_pages.profile_main_page import ProfileMainPage


@pytest.mark.ui
@allure.id("C6031344")
@allure.title("C6031344. Возможность для пользователя просматривать реквизиты карты 'GoR Classic'")
def test_ui_c60321344_user_can_view_card_classic_details(open_browser):
    # Авторизация пользователя
    MainPage(open_browser).authorization(phone_number=valid_phone_number_ui_python, password=valid_password)

    # Переход в личный кабинет(профиль)
    MainPage(open_browser).click_logo_gor()

    # Открытие вкладки 'Карты'
    ProfileMainPage(open_browser).open_profile_cards_page()

    # Кликнуть на изображение карты 'GoR Classic'
    ProfileCardsPage(open_browser).click_on_image_card_gor_classic()

    # Проверка отображения вкладки 'Информация'
    ProfileCardsPage(open_browser).check_display_tab_information()

    # Проверка отображения вкладки 'История'
    ProfileCardsPage(open_browser).check_display_tab_history()

    # Проверка отображения вкладки 'Управление'
    ProfileCardsPage(open_browser).check_display_tab_control()

    # Поверка отображения формы инфо о карте и ее элементов
    ProfileCardsPage(open_browser).check_full_fields_in_form_on_cards_page()

    # Проверка отображения кнопки Детали кредита
    ProfileCardsPage(open_browser).check_displaying_elements_on_page("button_card_money_transfer_loc")

    # Проверка отображения элементов Footer
    ProfileMainPage(open_browser).check_displaying_footer_elements()
