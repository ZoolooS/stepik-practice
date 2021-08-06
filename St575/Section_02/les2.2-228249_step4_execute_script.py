"""
https://stepik.org/lesson/228249/step/4?unit=200781
"""
# ====== imports block ================================== #
# import time
# import math
from selenium import webdriver
# from selenium.webdriver.support.ui import Select


# ====== function declaration =========================== #
# def calc(x):
#     return str(math.log(abs(12*math.sin(int(x)))))


# ====== main code ====================================== #
browser = webdriver.Chrome()
# browser.execute_script('alert("Robots at work");')
# browser.execute_script('document.title="Script executing";')
browser.execute_script("document.title='Script executing';alert('Robots at work');")

# time.sleep(10)
# browser.quit()

# ====== end of code ==================================== #
