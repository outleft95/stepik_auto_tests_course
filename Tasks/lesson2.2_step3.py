from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select
import os
import pyperclip

link = "https://suninjuly.github.io/file_input.html"
link2="https://stepik.org/lesson/228249/step/8?unit=200781"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("test@mail.ru")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'test.txt')
    input4 = browser.find_element(By.NAME, "file")
    input4.send_keys(file_path)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    alert = browser.switch_to.alert
    alert_text = alert.text
    addToClipBoard = alert_text.split(': ')[-1]
    pyperclip.copy(addToClipBoard)
    confirm = browser.switch_to.alert
    confirm.accept()
    browser.get(link2)
    time.sleep(30)
    browser.get(link2)
    time.sleep(15)
    nav = browser.find_element(By.TAG_NAME, "textarea")
    nav.send_keys(pyperclip.paste())
    button2 = browser.find_element(By.CLASS_NAME, "submit-submission")
    button2.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла