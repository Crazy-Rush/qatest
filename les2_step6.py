import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


link = 'http://suninjuly.github.io/execute_script.html'

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element(By.ID, 'input_value').text
    y = calc(x)
    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(y)
    robot_check = browser.find_element(By.ID, 'robotCheckbox')
    robot_check.click()
    robot_radio = browser.find_element(By.ID, 'robotsRule')
    browser.execute_script('return arguments[0].scrollIntoView(true);', robot_radio)
    robot_radio.click()
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    # browser.execute_script('return arguments[0].scrollIntoView(true);', button)
    button.click()

finally:
    time.sleep(5)
    browser.quit()
