import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger


class Cart_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    #  Locators
    cart_over = '//div[@class="confirm_box"]/a'   #  локатор "Оформить заказ"
    price = '//div[@id="basket_form_container"]/div/div[2]/div[3]/strong'   #  локатор цены указаной в корзине
    clear_cart_all = '//div[@class="confirm_box"]/a[@class="clear_basket"]'

    #  Getters
    '''Получение явного ожидания по вышеуказанным локаторам'''
    def get_cart_over(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_over)))

    def get_clear_cart_all(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.clear_cart_all)))

    def get_price(self):
        return self.driver.find_element(By.XPATH, self.price)

    #  Actions
    '''Действия'''

    def click_cart_over(self):   #  клик кнопки Оформить заказ
        self.driver_scroll("400")
        self.get_cart_over().click()
        print('Click "Оформление" in cart')

    def click_clear_cart_all(self):   #  клик кнопки Очистить корзину
        self.driver_scroll("400")
        self.get_clear_cart_all().click()
        print('Click "Очистить корзину"')

    def price_text_cart(self):    #  считывание цены указанной в корзине
        value = self.get_price().text
        val = value.replace(' руб.', '').replace(' ', '')
        return val

    #  Methods

    def select_cart_over(self):   #  переход на страницу оформления заказа
        with allure.step('select cart over'):
            Logger.add_start_step(method='select_cart_over')
            self.get_current_url()
            self.assert_url('https://www.rollingmoto.ru/personal/cart/')
            self.click_cart_over()
            time.sleep(5)
            Logger.add_end_step(url=self.driver.current_url, method='select_cart_over')

