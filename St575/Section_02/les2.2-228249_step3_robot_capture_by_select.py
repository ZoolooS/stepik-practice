"""
https://stepik.org/lesson/228249/step/3?unit=200781
"""
# ====== imports block ================================== #
import time
# import math
from selenium import webdriver
from selenium.webdriver.support.ui import Select


# ====== function declaration =========================== #
# def calc(x):
#     return str(math.log(abs(12*math.sin(int(x)))))


# ====== main code ====================================== #
# link = "http://suninjuly.github.io/selects1.html"
link = 'http://suninjuly.github.io/selects2.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element_by_id("num1").text
    num2 = browser.find_element_by_id("num2").text
    answer = int(num1) + int(num2)

    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(str(answer))

    browser.find_element_by_tag_name('button[type="submit"]').click()

finally:
    time.sleep(7)
    browser.quit()

# ====== end of code ==================================== #
