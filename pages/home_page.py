from time import sleep
import pytest
from selenium.webdriver.common.by import By
from constants.home_page_loc import *
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


@pytest.mark.usefixtures("setup")
class HomePage(PageBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def verify_homepage_opened(self,assertMessage):
        assert assertMessage in self.driver.current_url, f"Expected '{assertMessage}' to be in '{self.driver.current_url}'"
        
    def click_the_searchbox_and_enter_text(self,text):
        self.send_keys_element(SEARCHBOX,text)
        
    def click_search_icon(self):
        self.click_element(SEARCH_ICON)
        
    def verify_correct_data_searchbox(self,correct_data):
        searchbox=self.find_element(SEARCHBOX)
        assert correct_data in searchbox.get_attribute("value"),"The value entered in the search box is incorrect!"

    def verify_results_samsung(self,text):
            assert self.driver.title == text, f"The page title was expected to be '{text}', but it was found to be '{self.driver.title}'."






