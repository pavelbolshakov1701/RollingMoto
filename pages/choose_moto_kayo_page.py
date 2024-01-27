import time

import allure

from base.base_class import Base

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utilities.logger import Logger


class Choose_moto_page(Base):
    '''Выбор и применение фильтров с последующим переходом на страницу с выбранным мотоциклом'''


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    #  Locators

    filtr_price = '//div[@class="bx_filter_container"]/div/div/div[2]/a[2]'  #  локатор ползунок цены (правый)
    brend_product = '//*[text()="Бренд товара"]' #  локатор "Бренд"
    select_kayo = '//label[@for="WIZE_CATALOG_FILTER_351_2878062298"]/span' #  локатор Кауо
    enggine = '//*[text()="Кубатура, куб.см"]'  #  локатор Кубатура, куб.см
    select_enggine = '//label[@for="WIZE_CATALOG_FILTER_333_1548098294"]/span'  #  локатор 250
    type = '//*[text()="Тип"]'  #  локатор Тип
    select_type = '//label[@for="WIZE_CATALOG_FILTER_352_2978066050"]/span'   #  локатор Внедорожный
    froze = '//*[text()="Охлаждение"]'  #  локатор Охлаждение
    select_froze_air = '//label[@for="WIZE_CATALOG_FILTER_357_2771733348"]/span'   #  локатор Воздушное охлаждение
    select_froze_water = '//label[@for="WIZE_CATALOG_FILTER_357_859726709"]/span'   #  локатор охлаждение Жидкостное
    search = '//input[@id="set_filter"]'   #  локатор "Подобрать"
    kayo_t2_250_mx = '//div[@id="bx_3966226736_209222"]'   #  локатор Мотоцикл кроссовый KAYO T2 250 MX 21/18 (2022 г.) ПТС
    select_cart = '//div[@class="basket"]'   #  локатор переход в корзину
    add_cart = '//span[@class="item_buttons_counter_block"]/a'   #  локатор добавление мотоцикла в корзину
    price_moto = '//div[@class="pl_right"]/div/div[1]/div[2]/span'   #  локатор цены мотоцикла

    #  Getters
    '''Получение явного ожидания по вышеуказанным локаторам'''
    def get_filtr_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filtr_price)))

    def get_brend_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.brend_product)))

    def get_select_kayo(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_kayo)))

    def get_enggine(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.enggine)))

    def get_select_enggine(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_enggine)))

    def get_type(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.type)))

    def get_select_type(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_type)))

    def get_froze(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.froze)))

    def get_select_froze_air(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_froze_air)))

    def get_select_froze_water(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_froze_water)))

    def get_search(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.search)))

    def get_kayo_t2_250_mx(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.kayo_t2_250_mx)))

    def get_select_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.select_cart)))

    def get_add_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.add_cart)))

    def get_price_moto(self):
        value = self.driver.find_element(By.XPATH, self.price_moto)
        return value


     #  Actions
    '''Действия'''
    def polzunok(self):   #  перемещения ползунка цены влево
        self.action_chains().click_and_hold(self.get_filtr_price()).move_by_offset(-120, 0).release().perform()
        print('Перемещение ползунка цены')

    def choose_brend_KAYO(self):   #  выбор бренда мотоцикла
        self.get_brend_product().click()
        self.get_select_kayo().click()
        print('Choose "Бренд" --> "KAYO"')

    def choose_enggine_250(self):   #  выбор двигателя
        self.get_enggine().click()
        self.get_select_enggine().click()
        print('Choose "КУБАТУРА, КУБ.СМ" --> "250"')

    def choose_type(self):   #  выбор тип мотоцикла
        self.get_type().click()
        self.get_select_type().click()
        print('Choose "Тип" --> "Кроссовый"')

    def choose_froze(self):   #  выбор вариантов охлаждения двигателя
        self.get_froze().click()
        self.get_select_froze_air().click()
        self.get_select_froze_water().click()
        print('Choose "Охлаждение" --> "Воздушное" --> "Водяное"')

    def search_product(self):   #  клик кнопки подобрать
        self.get_search().click()
        print('Search product "Подобрать"')

    def choose_kayo_t2_250_mx(self):   #  наведение и клик мотоцикла с выбранными параметрами
        self.action_chains().move_to_element(self.get_kayo_t2_250_mx()).perform()
        self.get_kayo_t2_250_mx().click()
        print('Choose kayo t2 250 mx')

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
            self.polzunok()
            self.driver_scroll("400")
            self.choose_brend_KAYO()
            self.choose_enggine_250()
            self.driver_scroll("600")
            self.choose_type()
            self.driver_scroll("800")
            self.choose_froze()
            self.driver_scroll("1050")
            self.search_product()
            time.sleep(4)
            self.get_current_url()
            self.driver_scroll('450')
            self.choose_kayo_t2_250_mx()
            time.sleep(2)
            Logger.add_end_step(url=self.driver.current_url, method='filltr_moto')

    def kayo_MOTO(self):   #  действия с мотоциклом Kayo по выбранным параметрам
        with allure.step('kayo MOTO'):
            Logger.add_start_step(method='kayo_MOTO')
            self.get_current_url()
            self.assert_url('https://www.rollingmoto.ru/catalog/mototsikly_kayo/209222/')
            self.add_cart_action()
            time.sleep(2)
            self.select_cart_action()
            time.sleep(2)
            Logger.add_end_step(url=self.driver.current_url, method='kayo_MOTO')




