from functions.interactions import find_command,send_msg, read_first_contacts,end_bot
import time
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


# read responses 
with open ('docs\\botresponses.json',  encoding='utf-8') as f:
        read_j= f.read()

def main ():
   
    dic_resp = json.loads(read_j)
    cond = ''
    while cond != 'finalizar' :
        
        for rotate in range(8,11):
            
            time.sleep(1)
            read_first_contacts(rotate)

            com = find_command()
            resp = dic_resp.get(com)
            
            if resp != None: 
                send_msg(resp)
            
            if resp == 'bot finalizado': 
                time.sleep(2)
                cond = 'finalizar'
                break
    end_bot()

if __name__ == '__main__':
    main()
    