from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')
time.sleep(15)
contact = ['Meus linsk','Claudio Cavalcante']
msg = 'E aí meu viaado! '
#copyable-text selectable-text
def find_contact():
    print ('blz')

def send_msg():
    print ('enviado')


for contato in contact:
    find_contact(contact)
    send_msg(msg)