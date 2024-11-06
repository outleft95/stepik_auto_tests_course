from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select

def sum(x,y):
  return str(x+y)


link = "http://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.ID, "num1")
    x = int(x_element.text)
    y_element = browser.find_element(By.ID, "num2")
    y = int(y_element.text)
    z = sum(x,y)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(z)
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла