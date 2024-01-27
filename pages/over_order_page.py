import time

import allure
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger


class Over_order_page(Base):
    '''Страница финального оформления заказа'''


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #  Locators
    input_tel = '//input[@id="ORDER_PROP_3"]'   #  локатор поля ввода телефона
    input_adress = '//input[@id="ORDER_PROP_7"]'   #  локатор поля ввода адреса
    delivery = '//label[@for="ID_DELIVERY_ID_1107"]/i'   #  локатор радиокнопки доставки по Москве
    pay_system_sber = '//label[@for="ID_PAY_SYSTEM_ID_17"]/i'   #  локатор радиокнопки оплаты Сбербанк Онлайн
    information_massage = '//textarea[@id="ORDER_DESCRIPTION"]'   #  локатор поля ввода дополнительной информации и комментариев к заказу
    cart = '//div[@class="basket"]'   #  локатор корзины
    cart_clear = '//div[@class="bl"]/a[@class="bl_delete"]'#'//a[@data-id="ajaxaction=delete&ajaxaddid=209233"]'   #  локатор очистить содержимое корзины
    price_text_over = '//div[@class="last_price"]/span/strong'    #  локатор считывания итоговой стоимости товаров

    #  Getters
    '''Получение явного ожидания по вышеуказанным локаторам'''
    def get_input_tel(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.input_tel)))

    def get_input_adress(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.input_adress)))

    def get_pay_system_sber(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.pay_system_sber)))

    def get_delivery_moscow(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.delivery)))

    def get_information_massage(self):
        return  WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.information_massage)))

    def get_cart(self):
        return  WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart)))

    def get_clear_cart(self):
        return  WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_clear)))

    def get_price_text_over(self):
        value = self.driver.find_element(By.XPATH, self.price_text_over)
        return value

    #  Actions
    '''Действия'''

    def input_tel_action(self, tel):   #  наведение на поле и ввод телефона
        self.action_chains().move_to_element(self.get_input_tel()).perform()
        for i in range(14):
            self.get_input_tel().send_keys(Keys.BACKSPACE)
        self.get_input_tel().send_keys(tel)
        self.get_input_tel().send_keys(Keys.RETURN)
        print('Input "Телефон"')

    def input_adress_action(self, adress):   #  наведение на поле и ввод адресса
        self.action_chains().move_to_element(self.get_input_adress()).perform()
        self.get_input_adress().send_keys(adress)
        self.get_input_adress().send_keys(Keys.RETURN)
        print('Input "Адресс доставки"')

    def select_delivery_moscow(self):    #  выбор радиокнопки доставки по Москве и МО
        self.get_delivery_moscow().click()
        print('Select "Доставка по Москве и МО"')

    def select_pay_system_sber(self):   #  выбор радиокнопки оплаты через Сбербанк Онлайн
        self.driver.execute_script("arguments[0].click();", self.get_pay_system_sber())
        print('Select "Сбербанк Онлайн"')

    def information(self, message):    #  ввод дополнительной информации и комментариев к заказу
        self.get_information_massage().send_keys(message)
        self.get_information_massage().send_keys(Keys.RETURN)
        print('Input "Дополнительная информация" and message')

    def clear_cart_actions(self):    #  очистка содержимого корзины
        self.action_chains().move_to_element(self.get_cart()).perform()
        self.get_clear_cart().click()
        print('Click clear cart')

    def price_text_over_oop(self):   #  считывание итоговой стоимости
        value = self.get_price_text_over().text
        val = value.replace(' РУБ.', '').replace(' ', '')
        return val

    #  Methods

    def buy_moto(self):    #  заполнение данных страницы оформления заказа
        with allure.step('buy moto'):
            Logger.add_start_step(method='buy_moto')
            self.get_current_url()
            self.assert_url('https://www.rollingmoto.ru/personal/order/make/')
            self.input_tel_action(1234567890)
            time.sleep(1)
            self.input_adress_action('California, Los-Angeles')
            time.sleep(1)
            self.select_delivery_moscow()
            time.sleep(5)
            self.select_pay_system_sber()
            time.sleep(5)
            self.information('Просьба позвонить за час')
            time.sleep(3)
            Logger.add_end_step(url=self.driver.current_url, method='buy_moto')

