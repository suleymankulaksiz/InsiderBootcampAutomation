from selenium.webdriver.support import expected_conditions 
from selenium.webdriver.support.wait import WebDriverWait
from constants.home_page_loc import *
from selenium.webdriver.common.action_chains import ActionChains
import os
import allure

class PageBase:

    def __init__(self, driver):
        self.driver = driver
        
    def wait_element_visibility(self, locator):
        return WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))
        
    def click_element(self,locator):
        self.wait_element_visibility(locator).click()
    
    def send_keys_element(self,locator,text):
        self.wait_element_visibility(locator).send_keys(text)
        
    def accept_cookies(self):
        self.click_element(COOKIE)
    
    def find_element(self,locator):
        return self.driver.find_element(*locator)
    
    def find_elements(self,locator):
        return self.driver.find_elements(*locator)

    def doubleclick_element(self,locator):
        element = self.wait_element_visibility(locator)
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()
        
    def take_screenshot(self, screenshotName):
        file_path = os.path.join("images", screenshotName)
        self.driver.save_screenshot(file_path)
        
        with open(file_path, 'rb') as f:
            allure.attach(f.read(), name=screenshotName, attachment_type=allure.attachment_type.PNG)