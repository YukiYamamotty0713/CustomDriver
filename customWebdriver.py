from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time




class customDriver():
    
    #待機時間
    wait_time = 10
    
    def __init__(self,URL,headless=False):
        
        self.driver = webdriver.Chrome()
        self.url = URL
        self.wait = WebDriverWait(self.driver,self.wait_time)
        # if headless == True:
        #     self.driver.set_headless(headless)
            
    def open(self):
        '''
        Argument is not needed. information about URL 
        would be set as of generating instance of class.
        '''
        self.driver.get(self.url)        


    def input(self, By:By, element:str, text:str):
        '''
        simply input the text into the box.
        '''            
        box = self.wait.until(EC.presence_of_element_located((By, element)))
        box.send_keys(text)
        box.submit()

    def click(self, By:By, element:str):
        '''
        simply click the element.
        '''
        obj = self.wait.until(EC.presence_of_element_located((By, element)))
        obj.click()

    def accept_alert(self):
        '''
        accept alert until 10 minutes passed.
        '''
        alert = self.wait.until(EC.alert_is_present())
        alert.accept()
        time.sleep(1)
    
    
    def cancel_alert(self):
        '''
        cancel alert until 10 minutes passed.
        '''
        self.wait.until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert.dismiss()
        time.sleep(1)
           
    
    def destroy(self):
        self.driver.quit()

        
        

