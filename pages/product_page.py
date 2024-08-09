from time import sleep
import pytest
from constants.product_page_loc import *
from pages.base_page import *
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class ProductPage(PageBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver



    def verify_product_page(self, expectedAssert):
        item=self.find_element(PRODUCT_PAGE)
        item_assert=item.text
        assert expectedAssert in item_assert,f"Expected result '{expectedAssert}', but got '{item_assert}'"

    def click_add_to_cart_button(self):
        self.click_element(ADD_TO_CART_BUTTON)

    def verify_product_added_to_cart_and_present_on_cart_page(self,expectedAssert1,expectedAssert2):
        add_control=self.find_element(ADD_TO_CART_ASSERT)
        add_control_text=add_control.text
        assert expectedAssert1 in add_control_text,f"Expected result '{expectedAssert1}', but got '{add_control_text}'"
        basket_page=self.find_element(BASKET)
        basket_page_text=basket_page.text
        assert expectedAssert2 in basket_page_text,f"Expected result '{expectedAssert2}', but got '{basket_page_text}'"