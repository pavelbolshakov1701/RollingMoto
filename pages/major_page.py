import time

import allure

from base.base_class import Base

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utilities.logger import Logger

'''Создание класса главной страницы с авторизацией'''
class Major_page(Base):

    url = 'https://www.rollingmoto.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    #  Locators

    privacy_room = '//a[@class="profile"]' #  локатор "Личный кабинет"
    input_login = '//input[@name="USER_LOGIN"]' #  локатор поля ввода "Логин"
    input_password = '//input[@name="USER_PASSWORD"]' #  локатор поля ввода "Пароль"
    button_enter = '//a[@class="popup_button"]' #  локатор кнопки "Войти"
    button_moto = '//a[@href="/catalog/mototekhnika/"]' #  локатор кнопки "Мототехника"
    select_mototechnic = '//a[@href="/catalog/mototekhnika/"]' #  локатор кнопки мототехники
    select_moto = '//a[@href="/catalog/mototsikly/"]' #  локатор выпадающей кнопки "Мотоциклы"
    select_vezdehod = '//a[@href="/catalog/vnedorozhnye_mototsikly/"]' #  локатор выпадающей кнопки "Внедорожные мотоциклы"


    #  Getters
    '''Получение явного ожидания по вышеуказанным локаторам'''
    def get_privacy_room(self):  #  Личный кабинет
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.privacy_room)))

    def get_input_login(self):  #  Поле логин
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.input_login)))

    def get_input_password(self):  #  поле пароль
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.input_password)))

    def get_button_enter(self):  #  кнопка Войти
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_enter)))

    def get_button_moto(self):  #  кнопка Мототехника
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_moto)))

    def get_select_mototechnic(self):  #  кнопка Мототехника
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_mototechnic)))

    def get_select_moto(self):  #  выпадающая кнопка Мотоциклы
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_moto)))

    def get_select_vezdehod(self):  #  выпадающая кнопка Внедорожные мотоциклы
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_vezdehod)))


     #  Actions
    '''Действия'''
    def click_privacy_room(self):  #  клик Личный кабинет
        self.get_privacy_room().click()
        print('Button "Личный кабинет" click')

    def input_logins(self, login):  #  ввод логина
        self.get_input_login().send_keys(login)
        print('Input login')

    def input_passwords(self, password):   #  ввод пароля
        self.get_input_password().send_keys(password)
        print('Input password')

    def click_button_enter(self):  #  клик кнопки Войти
        self.get_button_enter().click()
        print('Button "ВОЙТИ" click')

    def click_button_moto(self):  #  клик Мототехника
        self.get_button_moto().click()
        print('Button "Мототехника" click')

    def select_vezdehod_moto(self):  #  клик Внедорожные мотоциклы
        self.action_chains().move_to_element(self.get_select_mototechnic()).perform()
        self.action_chains().move_to_element(self.get_select_moto()).perform()
        self.get_select_vezdehod().click()
        print('Select and click "Мототехника --> Мотоциклы --> Внедорожные мотоциклы"')

    #  Methods

    def authorization_and_select_moto(self):   #  Авторизация и дальнейший выбор категории
        with allure.step('authorization and select moto'):
            Logger.add_start_step(method='authorization_and_select_moto')
            self.driver.get(self.url)
            self.assert_url('https://www.rollingmoto.ru/')
            time.sleep(3)
            self.driver.maximize_window()  # Увеличение окна браузера
            self.get_current_url()
            self.click_privacy_room()
            self.input_logins('Pasha_1996')
            self.input_passwords('+74957360644')
            self.click_button_enter()
            time.sleep(1)
            self.select_vezdehod_moto()
            Logger.add_end_step(url=self.driver.current_url, method='authorization_and_select_moto')


