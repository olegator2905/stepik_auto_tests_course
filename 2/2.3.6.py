from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math
import os

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/redirect_accept.html"
browser.get(link)
try:
    button1 = browser.find_element(By.TAG_NAME, "button").click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x_element = browser.find_element(By.ID, 'input_value')
    x = int(x_element.text)
    y = str(calc(x))
    input1 = browser.find_element(By.ID, "answer").send_keys(y)
    button2 = browser.find_element(By.TAG_NAME, "button").click()
finally:
    time.sleep(10)
    browser.quit()