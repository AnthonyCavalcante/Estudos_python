from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager


class Browser:
    
    def __init__(self, driver):
        self.driver == driver
    
    
    def Chrome (self):
        driver = self.driver 
        
        return driver.get('https://web.whatsapp.com/')


def main ():
    print('teste')

if __name__ == '__main__':
    main()
    