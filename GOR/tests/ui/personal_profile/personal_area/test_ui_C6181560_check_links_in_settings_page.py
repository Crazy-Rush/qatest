import pytest

import allure
from test_data.ui.url_data import link_location_page
from test_framework.ui.data.user_data import valid_password, valid_phone_number_ui_python
from test_framework.ui.pages.main_pages.main_page import MainPage
from test_framework.ui.pages.personal_profile_pages.profile_settings_page import ProfileSettingsPage


@pytest.mark.ui
@allure.id("C6181560")
@allure.title("C6181560. Проверка ссылок на странице Настройки.")
def test_ui_c6181560_check_links_in_settings_page(open_browser):
    # Авторизация пользователя
    MainPage(open_browser).authorization(phone_number=valid_phone_number_ui_python, password=valid_password)

    # Вход в личный кабинет
    MainPage(open_browser).click_button_account()

    # Переход во вкладку "Настройки"
    ProfileSettingsPage(open_browser).open_profile_options_page()
    MainPage(open_browser).wait_logo_is_clickable()

    # Проверка работоспособности ссылки в блоке мой аккаунт
    ProfileSettingsPage(open_browser).click_on_link("link_how_deactivate_account_locator")
    ProfileSettingsPage(open_browser).check_page_after_link_click(link_location_page)

    # Возврат на страницу настроек
    MainPage(open_browser).click_button_account()
    ProfileSettingsPage(open_browser).open_profile_options_page()
    MainPage(open_browser).wait_logo_is_clickable()

    # Проверка работоспособности ссылки в блоке сменить имя
    ProfileSettingsPage(open_browser).click_on_link("link_in_change_fio_block_locator")

    # Возврат на страницу настроек
    MainPage(open_browser).click_button_account()
    ProfileSettingsPage(open_browser).open_profile_options_page()
    MainPage(open_browser).wait_logo_is_clickable()

    # Проверка работоспособности ссылки в блоке смена ФИО по иным причинам
    ProfileSettingsPage(open_browser).click_on_link("link_other_way_to_change_fio_block_locator")
