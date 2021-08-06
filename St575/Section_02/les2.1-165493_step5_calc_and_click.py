"""

"""
# ====== imports block ================================== #
import time
import math
from selenium import webdriver


# ====== function declaration =========================== #
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


# ====== main code ====================================== #
link = "http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_el = browser.find_element_by_id('input_value')
    x = x_el.text
    answer = calc(x)

    answer_field = browser.find_element_by_id('answer')
    answer_field.send_keys(answer)

    browser.find_element_by_id('robotCheckbox').click()
    browser.find_element_by_id('robotsRule').click()
    browser.find_element_by_tag_name('button[type="submit"]').click()

finally:
    time.sleep(5)
    browser.quit()

# ====== end of code ==================================== #
