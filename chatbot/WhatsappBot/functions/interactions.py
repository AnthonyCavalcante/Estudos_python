from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
import clipboard
import time
import json
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')

contact = ['Meus links']
#tempo necessário para escanear qr-code do whatsappWeb
time.sleep(10)

#escreve o nome do contato no campo de busca de contatos 
def find_contact(contact):
    #class="copyable-text selectable-text"
    search =  driver.find_element_by_xpath('//div[contains(@class, "copyable-text selectable-text")]')
    time.sleep(2)
    search.send_keys(contact)
    search.send_keys(Keys.ENTER)
    
# escreve e envia mensagem para contato
def send_msg(msg):
    find_textarea = driver.find_elements_by_xpath('//div[contains(@class, "copyable-text selectable-text")]')
    time.sleep(2)
    find_textarea[1].send_keys(msg)
    find_textarea[1].send_keys(Keys.ENTER)


#analisa última mensagem da conversa e armazena na variável    
def find_command():
 
    actions = ActionChains(driver)
    com_text = driver.find_elements_by_xpath('//span[contains(@class, "i0jNr selectable-text copyable-text")]')
    textList = com_text.pop()
   
    actions.double_click(textList)
    actions.click(textList)
    actions.key_down(Keys.CONTROL)
    actions.send_keys('c')
    actions.key_up(Keys.CONTROL)
    actions.perform()
    msg_received = clipboard.paste()

    return  msg_received

def read_first_contacts(position):
    actions = ActionChains(driver)
    top_contacts = driver.find_elements_by_xpath('//div[contains(@class, "_3OvU8")]')
    actions.click(top_contacts[position]).perform()


def end_bot():
    driver.quit()

