from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
import os

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/explicit_wait2.html')
try:
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    button1 = browser.find_element(By.TAG_NAME, "button").click()
    button2 = browser.find_element(By.ID, "solve")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button2)
    x_element = browser.find_element(By.ID, 'input_value')
    x = int(x_element.text)
    y = str(calc(x))
    input1 = browser.find_element(By.ID, "answer").send_keys(y)
    button2.click()
    number = browser.switch_to.alert
    print(number.text)
    number.accept()
finally:
    browser.quit()