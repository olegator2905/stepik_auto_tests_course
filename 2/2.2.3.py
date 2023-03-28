from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, 'num1')
    x = int(x_element.text)
    x1_element = browser.find_element(By.ID, 'num2')
    x1 = int(x1_element.text)
    y = x + x1

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_visible_text(str(y))

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()