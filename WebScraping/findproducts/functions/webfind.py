from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
import json
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

def find_products(site, id, product):
   
    driver.get(site)

    search = driver.find_element_by_class_name(id)
    search.send_keys(product)
    search.send_keys(Keys.ENTER)
