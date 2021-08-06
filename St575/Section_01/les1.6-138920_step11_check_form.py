"""

"""
# ====== imports block ================================== #
from selenium import webdriver
import time

# ====== function declaration =========================== #


# ====== main code ====================================== #
link = "http://suninjuly.github.io/registration2.html"
# link = "http://suninjuly.github.io/registration1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    f_name = browser.find_element_by_css_selector('.first_block .form-control.first')
    f_name.send_keys("Ivan")
    l_name = browser.find_element_by_css_selector('.first_block .form-control.second')
    l_name.send_keys("Ivanov")
    e_mail = browser.find_element_by_css_selector('.first_block .form-control.third')
    e_mail.send_keys("Ivanov.Ivan@mail.com")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(5)
    browser.quit()

# ====== end of code ==================================== #
