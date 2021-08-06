"""
https://stepik.org/lesson/228249/step/7?unit=200781
"""
# ====== imports block ================================== #
# import time
# import math
import os

# from selenium import webdriver
# from selenium.webdriver.support.ui import Select


# ====== function declaration =========================== #


# ====== main code ====================================== #
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, '_assets.tmp', 'booo.txt')
# element.send_keys(file_path)

print(file_path)
print(os.path.abspath(__file__))
print(os.path.abspath(os.path.dirname(__file__)))

# ====== end of code ==================================== #
