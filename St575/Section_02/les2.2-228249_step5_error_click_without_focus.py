"""
https://stepik.org/lesson/228249/step/5?unit=200781
"""
# ====== imports block ================================== #
import time
# import math
from selenium import webdriver
# from selenium.webdriver.support.ui import Select


# ====== function declaration =========================== #

# ====== main code ====================================== #
browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)

button = browser.find_element_by_tag_name("button")
time.sleep(3)
browser.execute_script("return arguments[0].scrollIntoView(true);", button)  # Без этого кнопка не видна и клика не будет
button.click()

# Другие примеры прокрутки скриптом
# browser.execute_script("window.scrollBy(0, 100);")

# time.sleep(10)
# browser.quit()

# ====== end of code ==================================== #
