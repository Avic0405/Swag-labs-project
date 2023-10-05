from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
import time
# Create a ChromeOptions instance
firefox_options = Options()
firefox_options.headless = False

driver = webdriver.Firefox(service=Service(executable_path=GeckoDriverManager().install()), options=firefox_options)

driver.get('https://www.saucedemo.com/')
time.sleep(5)

#In 20 line sending username
driver.find_element(By.XPATH,('//*[@id="user-name"]')).send_keys('standard_user')
time.sleep(3)

#In 24 line sending password
driver.find_element(By.XPATH,('//*[@id="password"]')).send_keys('secret_sauce')
time.sleep(3)

#In 28 line clicking on login button
driver.find_element(By.XPATH,('//*[@id="login-button"]')).click()
time.sleep(5)

#from line 33 to 48 clicking on add cart button

driver.find_element(By.XPATH,('//*[@id="add-to-cart-sauce-labs-backpack"]')).click()
time.sleep(2)

driver.find_element(By.XPATH,('//*[@id="add-to-cart-sauce-labs-bike-light"]')).click()
time.sleep(2)

driver.find_element(By.XPATH,('//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')).click()
time.sleep(2)

driver.find_element(By.XPATH,('//*[@id="add-to-cart-sauce-labs-fleece-jacket"]')).click()
time.sleep(2)

driver.find_element(By.XPATH,('//*[@id="add-to-cart-sauce-labs-onesie"]')).click()
time.sleep(2)

driver.find_element(By.XPATH,('//*[@id="add-to-cart-test.allthethings()-t-shirt-(red)"]')).click()
time.sleep(2)

# In 52 clicking on mycart button
driver.find_element(By.XPATH,('//*[@id="shopping_cart_container"]/a')).click()
time.sleep(5)

# wait = WebDriverWait(driver, 10)
cart_items = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="cart_contents_container"]')))
my_card_data=[]

for item in cart_items:
    data=(item.text)
    my_card_data.append(data)

# print(my_card_data)
items_name_in_mycart = ["Sauce Labs Backpack", "Sauce Labs Bolt T-Shirt", "Sauce Labs Onesie","Sauce Labs Bike Light","Sauce Labs Fleece Jacket","Test.allTheThings() T-Shirt (Red)"]  # Add the names of items you added


for i in items_name_in_mycart:
    for j in my_card_data:
        if i in j :
            print(f"{i}, added in cart!")
        else:
          print(f"{i}, not added in cart!")



driver.quit()

