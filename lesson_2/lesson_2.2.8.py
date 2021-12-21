import os
from selenium import webdriver
import time


try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"

    browser.get(link)

    browser.find_element_by_name("firstname").send_keys("Pavel")
    browser.find_element_by_name("lastname").send_keys("Gorshkov")
    browser.find_element_by_name("email").send_keys("pavel@mail.ru")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file_pavel.txt')
    browser.find_element_by_id("file").send_keys(file_path)

    browser.find_element_by_tag_name("button").click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
