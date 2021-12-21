from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/explicit_wait2.html"

    browser.get(link)

    WebDriverWait(browser, 12).until(expected_conditions.text_to_be_present_in_element((By.ID, "price"), "$100"))

    browser.find_element_by_id("book").click()

    x = browser.find_element_by_id("input_value").text
    y = calc(x)

    browser.find_element_by_tag_name("input").send_keys(y)

    browser.find_element_by_id("solve").click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
