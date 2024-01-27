import time

import allure
import pytest

from base.base_class import Base
from pages.major_page import Major_page
from pages.choose_moto_kayo_page import Choose_moto_page
from pages.over_order_page import Over_order_page
from pages.cart_page import Cart_page
from pages.choose_ataki_moto import Choose_moto_page_ataki

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@allure.description('test buy moto_KAYO t2')
@pytest.mark.run(order=2)
def test_buy_moto_KAYO_t2(set_up):
    options = webdriver.ChromeOptions()
    # options.page_load_strategy = 'eager'
    options.add_experimental_option("detach", True)
    g = Service('C:\\Users\\User\\Desktop\\phyton\\resource\\chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=g)

    b = Base(driver)

    mp = Major_page(driver)
    mp.authorization_and_select_moto()

    cmp = Choose_moto_page(driver)
    cmp.filltr_moto()
    value_cmp = cmp.price_text_cmp()
    cmp.kayo_MOTO()

    cp = Cart_page(driver)
    value_cp = cp.price_text_cart()
    b.assert_comparison_word(value_cmp, value_cp)
    cp.select_cart_over()

    oop = Over_order_page(driver)
    value_oop = oop.price_text_over_oop()
    oop.buy_moto()
    b.assert_comparison_word(value_cmp, value_oop)

    b.screenshot()
    oop.clear_cart_actions()
    driver.quit()

@allure.description('test buy moto ataki')
@pytest.mark.run(order=1)
def test_buy_moto_ataki(set_up, one_moto):
    options = webdriver.ChromeOptions()
    # options.page_load_strategy = 'eager'
    options.add_experimental_option("detach", True)
    g = Service('C:\\Users\\User\\Desktop\\phyton\\resource\\chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=g)

    b = Base(driver)

    mp = Major_page(driver)
    mp.authorization_and_select_moto()

    cmpa = Choose_moto_page_ataki(driver)
    cmpa.filltr_moto()
    value_cmp = cmpa.price_text_cmp()
    cmpa.ataki_MOTO()

    cp = Cart_page(driver)
    value_cp = cp.price_text_cart()
    b.assert_comparison_word(value_cmp, value_cp)
    cp.select_cart_over()

    oop = Over_order_page(driver)
    value_oop = oop.price_text_over_oop()
    oop.buy_moto()
    b.assert_comparison_word(value_cmp, value_oop)

    b.screenshot()
    cmpa.select_cart_action()
    time.sleep(2)
    cp.click_clear_cart_all()
    driver.quit()




