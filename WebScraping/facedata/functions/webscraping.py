from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
import json
import time
from csv import DictReader

with open('docs\\urls.json') as f:
    read_json = f.read()


urls = json.loads(read_json)

driver = webdriver.Chrome(ChromeDriverManager().install())


def faceads():
    driver.get(urls.get('faceads'))
   
    mylogin= 'anthonycavalcante@gmail.com'
    mypassword = 'moiu1611'
    
    # acessa facebook
    flogin = driver.find_element_by_id("email")
    flogin.send_keys(mylogin)

    fpass = driver.find_element_by_id("pass")
    fpass.send_keys(mypassword)
    fpass.send_keys(Keys.ENTER)
    time.sleep(2)

    actions = ActionChains(driver)
    actions.send_keys((Keys.TAB)*20).send_keys(Keys.ENTER).perform()
    time.sleep(1)
    actions.send_keys(Keys.ENTER).perform()



    '''exportbtn = driver.find_element(By.XPATH, '//span[contains(@id, "export_button")]')
    exportbtn.click()
    time.sleep(1)
    exportbtn.send_keys(Keys.ENTER)
'''
def googleads():
    driver.get(urls.get('googedrive'))

    login = "anthonycavalcante@gmail.com"
    senha = "16maju11"





def end_game():
    driver.close()