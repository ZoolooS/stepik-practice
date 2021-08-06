"""
https://stepik.org/lesson/228249/step/8?unit=200781
"""
# ====== imports block ================================== #
import os
import time
# import math

from selenium import webdriver
# from selenium.webdriver.support.ui import Select


# ====== function declaration =========================== #


# ====== main code ====================================== #
link = 'http://suninjuly.github.io/file_input.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_css_selector('input[name="firstname"]').send_keys('Ivan')
    browser.find_element_by_css_selector('input[name="lastname"]').send_keys('Ivanov')
    browser.find_element_by_css_selector('input[name="email"]').send_keys('Ivanov.Ivan@mail.com')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, '_assets.tmp', 'booo.txt')
    browser.find_element_by_id('file').send_keys(file_path)

    browser.find_element_by_css_selector('button[type="submit"]').click()

finally:
    time.sleep(7)
    browser.quit()

# ====== end of code ==================================== #
