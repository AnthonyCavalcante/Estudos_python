from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')

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
    