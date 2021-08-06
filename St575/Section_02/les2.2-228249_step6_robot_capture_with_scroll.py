"""
https://stepik.org/lesson/228249/step/6?unit=200781
"""
# ====== imports block ================================== #
import time
import math
from selenium import webdriver
# from selenium.webdriver.support.ui import Select


# ====== function declaration =========================== #
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


# ====== main code ====================================== #
link = "https://SunInJuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element_by_id('input_value').text
    answer = calc(x)

    browser.find_element_by_id('answer').send_keys(answer)

    button = browser.find_element_by_css_selector('button[type="submit"]')
    browser.execute_script('return arguments[0].scrollIntoView(true);', button)
    robot_checkbox = browser.find_element_by_id('robotCheckbox').click()
    robot_radio = browser.find_element_by_id('robotsRule').click()
    button.click()

finally:
    time.sleep(7)
    browser.quit()

# ====== end of code ==================================== #
