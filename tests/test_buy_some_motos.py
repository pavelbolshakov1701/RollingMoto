import time

import allure

from base.base_class import Base
from pages.major_page import Major_page
from pages.choose_moto_kayo_page import Choose_moto_page
from pages.over_order_page import Over_order_page
from pages.cart_page import Cart_page
from pages.choose_ataki_moto import Choose_moto_page_ataki

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@allure.description('test buy some motos')
def test_buy_some_motos(set_up, some_moto):
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
    kayo1 = cmp.price_text_cmp()
    cmp.kayo_MOTO()

    mp.select_vezdehod_moto()

    cmpa = Choose_moto_page_ataki(driver)
    cmpa.filltr_moto()
    ataki1 = cmpa.price_text_cmp()
    cmpa.ataki_MOTO()

    cp = Cart_page(driver)
    total_cart = int(cp.price_text_cart())
    total = int(ataki1) + int(kayo1)
    b.assert_comparison_word(total, total_cart)

    cp.select_cart_over()

    oop = Over_order_page(driver)
    value_oop = int(oop.price_text_over_oop())
    oop.buy_moto()
    b.assert_comparison_word(total_cart, value_oop)

    b.screenshot()
    cmp.select_cart_action()
    time.sleep(2)
    cp.click_clear_cart_all()
    driver.quit()