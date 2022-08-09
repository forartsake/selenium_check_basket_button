
from selenium.webdriver.common.by import By
import time

link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_if_webpage_has_add_basket_button(browser):
    browser.get(link)
    time.sleep(10)
    el_lst = browser.find_elements(By.CSS_SELECTOR, "button.btn-add-to-basket")
    assert len(el_lst) > 0, "basket button does not exist"


