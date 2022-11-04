import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://suninjuly.github.io/alert_accept.html'
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn').click()
    alert = browser.switch_to.alert
    alert.accept()
    x_el = browser.find_element(By.ID, 'input_value').text
    y = calc(x_el)
    input1 = browser.find_element(By.ID, 'answer').send_keys(y)
    button1 = browser.find_element(By.CSS_SELECTOR, 'button.btn').click()


finally:
    time.sleep(5)
    browser.quit()