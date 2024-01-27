import time

import allure

from base.base_class import Base

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utilities.logger import Logger


class Choose_moto_page_ataki(Base):
    '''Выбор и применение фильтров с последующим переходом на страницу с выбранным мотоциклом'''


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    #  Locators

    ataki_moto = '//div[@id="bx_3966226736_215940"]'   #  локатор Мотоцикл кроссовый Ataki
    select_cart = '//div[@class="basket"]'   #  локатор переход в корзину
    add_cart = '//span[@class="item_buttons_counter_block"]/a'   #  локатор добавление мотоцикла в корзину
    price_moto = '//div[@class="pl_right"]/div/div/div//span[@data-offer-id="215943"]'   #  локатор цены мотоцикла

    #  Getters
    '''Получение явного ожидания по вышеуказанным локаторам'''

    def get_ataki_moto(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.ataki_moto)))

    def get_select_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.select_cart)))

    def get_add_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.add_cart)))

    def get_price_moto(self):
        value = self.driver.find_element(By.XPATH, self.price_moto)
        return value


     #  Actions
    '''Действия'''

    def choose_ataki_moto(self):   #  наведение и клик мотоцикла с выбранными параметрами
        self.action_chains().move_to_element(self.get_ataki_moto()).perform()
        self.get_ataki_moto().click()
        print('Choose ataki')

    def add_cart_action(self):   #  добавление выбранного мотоцикла в корзину
        self.get_add_cart().click()
        print('Add to cart "В корзину"')

    def select_cart_action(self):   #  переход в корзину
        self.get_select_cart().click()
        print('Get cart "Корзина"')

    def price_text_cmp(self):    #  считывание цены мотоцикла
        value = self.get_price_moto().text
        val = value.replace(' руб.', '').replace(' ', '')
        return val


    #  Methods

    def filltr_moto(self):    #  выбор и применение фильтров
        with allure.step('filltr moto'):
            Logger.add_start_step(method='filltr_moto')
            self.get_current_url()
            self.assert_url('https://www.rollingmoto.ru/catalog/vnedorozhnye_mototsikly/')
            time.sleep(4)
            self.driver_scroll('450')
            self.choose_ataki_moto()
            time.sleep(2)
            Logger.add_end_step(url=self.driver.current_url, method='filltr_moto')

    def ataki_MOTO(self):   #  действия с мотоциклом Ataki по выбранным параметрам
        with allure.step('ataki MOTO'):
            Logger.add_start_step(method='ataki_MOTO')
            self.get_current_url()
            self.assert_url('https://www.rollingmoto.ru/catalog/mototsikly_ataki/215940/')
            self.add_cart_action()
            time.sleep(2)
            self.select_cart_action()
            time.sleep(2)
            Logger.add_end_step(url=self.driver.current_url, method='ataki_MOTO')




