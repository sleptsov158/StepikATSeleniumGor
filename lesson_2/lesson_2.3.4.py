import os
from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/alert_accept.html"

    browser.get(link)

    browser.find_element_by_tag_name("button").click()
    browser.switch_to.alert.accept()

    x = browser.find_element_by_id("input_value").text
    y = calc(x)

    browser.find_element_by_tag_name("input").send_keys(y)

    browser.find_element_by_tag_name("button").click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
