import pytest
from constants.category_page_loc import *
from pages.base_page import *
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures("setup")
class CategoryPage(PageBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_second_page(self):
        self.click_element(SECOND_PAGE)
    
    def verify_second_page_clicked(self,expectedAssert):
        current_url = self.driver.current_url
        assert expectedAssert in current_url,f"Expected '{expectedAssert}' to be in '{self.driver.current_url}'"
        secondPage = self.wait_element_visibility(VERIFY_SECOND_PAGE)
        self.driver.execute_script("arguments[0].scrollIntoView();", secondPage)       
        self.take_screenshot("verifySecondPageClicked.png")
        self.driver.execute_script("window.scrollTo(0, 0);")

    def click_product_from_list(self):
        #Burada sayfada yer alan sponsor etiketine sahip ürünleri filtreleme işlemi yaparak tıklamanın başarılı olması sağlanmıştır.
        all_products = self.find_elements(ALL_PRODUCT)
        not_sponsored_products = []
        for product in all_products:
            sponsor_label = product.find_elements(By.CSS_SELECTOR, f'.{sponsored_products_text}')
            if not sponsor_label:  
                not_sponsored_products.append(product)
        if len(not_sponsored_products) >= 21:
                target_product = not_sponsored_products[20]
                target_product.find_element(By.CSS_SELECTOR, 'h2 a').click()
                print(f"Ürüne tıklama başarılı: Konum {21}.")
        else:
            print(f"Ürüne tıklama işlemi başarılı değildir.{21}.")



