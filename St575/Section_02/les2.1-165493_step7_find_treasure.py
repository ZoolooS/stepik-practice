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
link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    chest = browser.find_element_by_id("treasure")
    chest_val = chest.get_attribute("valuex")
    answer = calc(chest_val)

    browser.find_element_by_id('answer').send_keys(answer)

    browser.find_element_by_id('robotCheckbox').click()
    browser.find_element_by_id('robotsRule').click()
    browser.find_element_by_tag_name('button[type="submit"]').click()

finally:
    time.sleep(7)
    browser.quit()

# ====== end of code ==================================== #
