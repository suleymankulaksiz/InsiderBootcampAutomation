from time import sleep
import pytest
from constants.category_page_loc import *
from pages.base_page import *


@pytest.mark.usefixtures("setup")
class CategoryPage(PageBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_second_page(self):
        self.click_element(SECOND_PAGE)
    
    def verify_second_page_clicked(self,expectedAssert):
        self.driver.implicitly_wait(10)
        current_url = self.driver.current_url
        assert expectedAssert in current_url,f"Expected '{expectedAssert}' to be in '{self.driver.current_url}'"
    
    def click_product(self):
        self.click_element(PRODUCT)
    
    





