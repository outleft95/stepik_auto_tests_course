from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    img = browser.find_element(By.TAG_NAME, "img")
    x=img.get_attribute("valuex")
    y = calc(x)  
    input1 = browser.find_element(By.CSS_SELECTOR, "input#answer:required")
    input1.send_keys(y)
    checkbox = browser.find_element(By.CSS_SELECTOR, "[id='robotCheckbox']")
    checkbox.click()
    radiobutton = browser.find_element(By.CSS_SELECTOR, "[id='robotsRule']")
    radiobutton.click()
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла