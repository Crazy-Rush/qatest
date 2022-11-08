import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By




link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_guest_should_see_buy_button(browser):
    browser.get(link)
    time.sleep(30)
    select_button = browser.find_elements(By.CSS_SELECTOR, 'btn-primary')
    assert select_button is not None, 'Селектор не найден.'

