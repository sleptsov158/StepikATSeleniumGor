from selenium.webdriver.support.ui import Select
import time
from selenium import webdriver


def calc(x, y):
    return str(int(x) + int(y))


link = "http://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element_by_id("num1").text
    num2 = browser.find_element_by_id("num2").text

    y = calc(num1, num2)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text(y)

    button = browser.find_element_by_tag_name("button")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
