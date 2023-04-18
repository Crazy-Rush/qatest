import pytest

import allure
from test_framework.ui.data.user_data import password, valid_password, valid_phone_number_ui_python
from test_framework.ui.pages.main_pages.main_page import MainPage
from test_framework.ui.pages.personal_profile_pages.profile_general_information_page import (
    ProfileGeneralInformationPage,
)
from test_framework.ui.pages.personal_profile_pages.profile_security_page import ProfileSecurityPage
from test_framework.ui.pages.profile_pages.profile_main_page import ProfileMainPage


@pytest.mark.ui
@allure.id("C6176286")
@allure.title("C6176286. Успешное изменение пароля в личном кабинете.")
def test_ui_C6176286_success_change_password(browser_change_password_after_test):
    # Авторизация пользователя
    MainPage(browser_change_password_after_test).authorization(
        phone_number=valid_phone_number_ui_python, password=valid_password
    )

    # Вход в личный кабинет
    ProfileMainPage(browser_change_password_after_test).open_profile_general_information_page()

    # Клик на вкладку "Безопасность"
    ProfileGeneralInformationPage(browser_change_password_after_test).open_profile_security_page()

    # Клик на кнопку "Изменить пароль"
    ProfileSecurityPage(browser_change_password_after_test).click_on_button_change_password()

    # Ввод текущего пароля
    ProfileSecurityPage(browser_change_password_after_test).enter_current_password(valid_password)

    # Проверка введенного текста
    ProfileSecurityPage(browser_change_password_after_test).check_fields_value(
        "field_current_password_locator", valid_password
    )

    # Нажатие на кнопку "глаза" и проверка, что нажатие случилось
    ProfileSecurityPage(browser_change_password_after_test).click_on_button_eye("button_eye_current_password_locator")
    ProfileSecurityPage(browser_change_password_after_test).check_state_button_eye("field_current_password_locator")

    # Ввод нового пароля
    ProfileSecurityPage(browser_change_password_after_test).enter_new_password(password)

    # Нажатие на кнопку "глаза" и проверка, что нажатие случилось
    ProfileSecurityPage(browser_change_password_after_test).click_on_button_eye(
        "button_eye_create_new_password_locator"
    )
    ProfileSecurityPage(browser_change_password_after_test).check_state_button_eye("field_create_new_password_locator")

    # Ввод поддтверждения пароля
    ProfileSecurityPage(browser_change_password_after_test).enter_confirm_new_password(password)

    # Нажатие на кнопку "глаза" и проверка, что нажатие случилось
    ProfileSecurityPage(browser_change_password_after_test).click_on_button_eye(
        "button_eye_confirm_new_password_locator"
    )
    ProfileSecurityPage(browser_change_password_after_test).check_state_button_eye("field_confirm_new_password_locator")

    # Нажатие на кнопку подтвердить
    ProfileSecurityPage(browser_change_password_after_test).click_submit_button()
