import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


link = 'http://suninjuly.github.io/cats.html'


try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element(By.ID, "button")
    # new_window = browser.window_handles[1]
    # browser.switch_to.window(new_window)
    #
    # x = browser.find_element(By.ID, 'input_value').text
    # y = calc(x)
    # input1 = browser.find_element(By.ID, 'answer')
    # input1.send_keys(y)
    # button = browser.find_element(By.CSS_SELECTOR, 'button.btn').click()

finally:
    time.sleep(5)
    browser.quit()