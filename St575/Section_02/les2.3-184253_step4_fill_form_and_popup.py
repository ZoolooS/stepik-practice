"""
https://stepik.org/lesson/184253/step/4?unit=158843
"""
# ====== imports block ================================== #
# import os
import time
import math

from selenium import webdriver
# from selenium.webdriver.support.ui import Select


# ====== function declaration =========================== #
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


# ====== main code ====================================== #
link = 'http://suninjuly.github.io/alert_accept.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_css_selector('button[type="submit"]').click()
    time.sleep(1)

    browser.switch_to.alert.accept()

    x = browser.find_element_by_id('input_value').text
    answer = calc(x)

    browser.find_element_by_id('answer').send_keys(answer)
    browser.find_element_by_css_selector('button[type="submit"]').click()

finally:
    time.sleep(7)
    browser.quit()

# alert = browser.switch_to.alert
# alert_text = alert.text
# alert.accept()

# confirm = browser.switch_to.alert
# confirm.dismiss()

# prompt = browser.switch_to.alert
# prompt.send_keys("My answer")
# prompt.accept()

# ====== end of code ==================================== #
