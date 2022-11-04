import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = 'http://suninjuly.github.io/get_attribute.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    pic = browser.find_element(By.ID, 'treasure')
    x = pic.get_attribute('valuex')
    y = calc(x)
    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(y)
    robot_check = browser.find_element(By.ID, 'robotCheckbox')
    robot_check.click()
    robot_radio = browser.find_element(By.ID, 'robotsRule')
    robot_radio.click()
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()


finally:
    time.sleep(5)
    browser.quit()