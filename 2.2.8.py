from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time
import os
# def calc(x):
#     return str(math.log(abs(12 * math.sin(int(x)))))
#     #link = "http://suninjuly.github.io/registration1.html"

# link = "https://suninjuly.github.io/file_input.html"
# browser = webdriver.Chrome()
# browser.get(link)

try:
    link = "https://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    input = browser.find_element(By.NAME, 'firstname').send_keys("Anna")

    input = browser.find_element(By.NAME, 'lastname').send_keys("DEV")

    input = browser.find_element(By.NAME, 'email').send_keys("businka@mur-mur.com")
    file_path = '/Users/annanine/Desktop/untitled folder/python.txt'
    upload_element = browser.find_element(By.NAME, 'file')
    upload_element.send_keys(file_path)

    option3 = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    option3.click()

finally:
    time.sleep(5)

    browser.quit()