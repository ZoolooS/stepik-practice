"""

"""
# ====== imports block ================================== #
import time

from selenium import webdriver

# ====== function declaration =========================== #


# ====== main code ====================================== #
link = "http://suninjuly.github.io/huge_form.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    elements = browser.find_elements_by_tag_name('input[type="text"]')
    for element in elements:
        element.send_keys("Мой ответ")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()
finally:
    time.sleep(10)
    browser.quit()

# ====== end of code ==================================== #
