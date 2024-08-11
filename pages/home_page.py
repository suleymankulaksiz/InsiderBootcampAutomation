import pytest
from constants.home_page_loc import *
from pages.base_page import *

@pytest.mark.usefixtures("setup")
class HomePage(PageBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def verify_homepage_opened(self,assertMessage):
        assert assertMessage == self.driver.current_url, f"Expected '{assertMessage}' to be in '{self.driver.current_url}'"
        self.take_screenshot("verifyHomepageOpened.png") 
        
    def click_the_searchbox_and_enter_text(self,text):
        self.send_keys_element(SEARCHBOX,text)
        
    def click_search_icon(self):
        self.click_element(SEARCH_ICON)
        
    def verify_searchbox_text(self,correct_data):
        searchbox=self.find_element(SEARCHBOX)
        assert correct_data in searchbox.get_attribute("value"),"The value entered in the search box is incorrect!"
        self.take_screenshot("verifySearchboxText.png")

    def verify_results_samsung(self,text):
            assert self.driver.title in text, f"The page title was expected to be '{text}', but it was found to be '{self.driver.title}'."
            self.take_screenshot("verifyResultsSamsung.png")







