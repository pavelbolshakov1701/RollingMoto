import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.select import Select

from base.base_class import Base

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
# options.page_load_strategy = 'eager'
options.add_experimental_option("detach", True)
g = Service('C:\\Users\\User\\Desktop\\phyton\\resource\\chromedriver.exe')
driver = webdriver.Chrome(options=options, service=g)


url = 'https://www.rollingmoto.ru/'
# url = 'https://www.rollingmoto.ru/catalog/mototsikly_kayo/209222/'
# url = 'https://www.rollingmoto.ru/personal/cart/'
driver.get(url)
time.sleep(5)

# v = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[text()="Мотоцикл кроссовый KAYO T2 250 MX 21/18 (2022 г.) ПТС"]')))
# s = v.text
# print(s)

# v = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//div[@class="item_current_price"]/span')))
# s = v.text
# print(s)

# v = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//tr[@class="product-tr"]/td[3]/div')))
# s = v.text
# print(s)
# //tr[@class="product-tr"]/td[3]/div



privacy_room = '//a[@class="profile"]'
# i = driver.find_element(By.XPATH, )
# driver.switch_to
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//a[@class="profile"]'))).click()
WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//input[@name="USER_LOGIN"]'))).send_keys('Pasha_1996')
WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//input[@name="USER_PASSWORD"]'))).send_keys('+74957360644')
WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//a[@class="popup_button"]'))).click()
time.sleep(7)

# WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//a[@href="/catalog/mototekhnika/"]')))
# WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//a[@href="/catalog/mototsikly/"]')))
actions = ActionChains(driver)
z = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//a[@href="/catalog/mototekhnika/"]')))
actions.move_to_element(z).perform()
s = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//a[@href="/catalog/mototsikly/"]')))
actions.move_to_element(s).perform()
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//a[@href="/catalog/vnedorozhnye_mototsikly/"]'))).click()
# time.sleep(5)

# //*[text()='Мототехника']/../ul/li[2]/div/ul/li[2]/a
# //div[@class="bx_filter_container"]/div/div/div[2]/a[2]

'''NEXT PAGE'''
x = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//div[@class="bx_filter_container"]/div/div/div[2]/a[2]')))
# actions.move_to_element(x).perform()
actions.click_and_hold(x).move_by_offset(-120, 0).release().perform()
driver.execute_script('window.scrollTo(0, 400)')
# time.sleep(2)
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[text()="Бренд товара"]'))).click()
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//label[@for="WIZE_CATALOG_FILTER_351_2878062298"]/span'))).click()
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[text()="Кубатура, куб.см"]'))).click()
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//label[@for="WIZE_CATALOG_FILTER_333_1548098294"]/span'))).click()
driver.execute_script('window.scrollTo(0, 600)')
# time.sleep(2)
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[text()="Тип"]'))).click()
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//label[@for="WIZE_CATALOG_FILTER_352_2978066050"]/span'))).click()
driver.execute_script('window.scrollTo(0, 800)')
# time.sleep(2)
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[text()="Охлаждение"]'))).click()
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//label[@for="WIZE_CATALOG_FILTER_357_2771733348"]/span'))).click()
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//label[@for="WIZE_CATALOG_FILTER_357_859726709"]/span'))).click()
driver.execute_script('window.scrollTo(0, 1050)')
# time.sleep(2)
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//input[@id="set_filter"]'))).click()


'''NEXT PAGE'''

actions.move_to_element(WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//div[@id="bx_3966226736_209222"]')))).perform()
# time.sleep(2)
WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//div[@id="bx_3966226736_209222"]'))).click()
driver.execute_script('window.scrollTo(0, 200)')
v = driver.find_element(By.XPATH, '//div[@class="pl_right"]/div/div[1]/div[2]/span')
s = v.text
print(s)
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//span[@class="item_buttons_counter_block"]/a'))).click()
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//div[@class="basket"]/a'))).click()
b = driver.find_element(By.XPATH, '//div[@id="basket_form_container"]/div/div[2]/div[3]/strong')
n = b.text
print(s)
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//div[@class="confirm_box"]/a'))).click()
time.sleep(7)

'''NEXT PAGE'''

actions.move_to_element(WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//input[@id="ORDER_PROP_3"]')))).perform()
time.sleep(2)
for i in range(14):
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//input[@id="ORDER_PROP_3"]'))).send_keys(Keys.BACKSPACE)
# WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//input[@id="ORDER_PROP_3"]'))).send_keys(Keys.LEFT_CONTROL)
WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//input[@id="ORDER_PROP_3"]'))).send_keys(1234567890)
time.sleep(3)
actions.move_to_element(WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//input[@id="ORDER_PROP_7"]')))).perform()
WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//input[@id="ORDER_PROP_7"]'))).send_keys('lskdk')
time.sleep(3)
WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//label[@for="ID_DELIVERY_ID_1107"]/i'))).click()
time.sleep(4)
# actions.move_to_element(WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//label[@for="ID_PAY_SYSTEM_ID_17"]/i')))).perform()
driver.execute_script("arguments[0].click();", WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//label[@for="ID_PAY_SYSTEM_ID_17"]/i'))))
time.sleep(7)
# actions.move_to_element(WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//textarea[@id="ORDER_DESCRIPTION"]')))).perform()
WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//textarea[@id="ORDER_DESCRIPTION"]'))).send_keys('Просьба позвонить за час')
actions.move_to_element(WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//div[@class="bx_ordercart_order_pay_center"]/p/a')))).perform()

# p = driver.find_element(By.XPATH, '//div[@class="last_price"]/span/strong')
# l = p.text
# print(s)

# n = '164 990 руб.'
# print(n)
# h = n.replace(' руб.', '').replace(' ', '')
# print(h)