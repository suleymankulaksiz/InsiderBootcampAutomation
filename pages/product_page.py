import pytest
from constants.product_page_loc import *
from pages.base_page import *

@pytest.mark.usefixtures("setup")
class ProductPage(PageBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def verify_product_page(self, expectedAssert):
        item=self.find_element(PRODUCT_PAGE)
        item_assert=item.text
        assert expectedAssert in item_assert,f"Expected result '{expectedAssert}', but got '{item_assert}'"
        self.take_screenshot("verifyProductPage.png")

    def click_add_to_cart_button(self):
        self.click_element(ADD_TO_CART_BUTTON)

    def verify_product_added_to_cart_and_present_on_cart_page(self,expectedAssert1,expectedAssert2):
        add_control=self.find_element(ADD_TO_CART_ASSERT)
        add_control_text=add_control.text
        assert expectedAssert1 in add_control_text,f"Expected result '{expectedAssert1}', but got '{add_control_text}'"
        basket_page=self.find_element(BASKET)
        basket_page_text=basket_page.text
        assert expectedAssert2 in basket_page_text,f"Expected result '{expectedAssert2}', but got '{basket_page_text}'"
        self.take_screenshot("verifyAddProductAndCartPage.png")
    
    def click_amazon_logo(self):
        self.click_element(LOGO)
        
    def verify_returned_to_homepage(self,assertMessage):
        assert assertMessage in self.driver.current_url, f"Expected '{assertMessage}' to be in '{self.driver.current_url}'"
        self.take_screenshot("verifyReturnedHomepage.png")