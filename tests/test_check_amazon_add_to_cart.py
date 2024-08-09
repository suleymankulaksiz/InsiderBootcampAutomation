from time import sleep
import pytest
from pages.home_page import *
from pages.category_page import *
from pages.product_page import *

@pytest.mark.usefixtures("setup")
class TestProcess():
    
    def test_check_add_product_to_cart(self):
        #Burada yer alan kodlar anasayfadaki işlemleri gerçekleştirmek içindir.
        home_page= HomePage(self.driver)
        home_page.accept_cookies()                                  #Çerez kabul edilir.
        home_page.verify_homepage_opened("amazon.com.tr")           #current_url alınarak title doğrulaması ile anasayfada olduğumuz kontrol edilir.
        home_page.click_the_searchbox_and_enter_text("Samsung")     #Arama kutsuna tıklanır ve Samsung ifadesi girilir.
        home_page.verify_correct_data_searchbox("Samsung")          #Searchbox alanına, doğru verinin girildiği kontrol edilir.
        home_page.click_search_icon()                               #Arama ikonuna tıklanır.
        home_page.verify_results_samsung("Amazon.com.tr : Samsung") #Samsung için sonuç bulduğu kontrol edilir.
        
        #Burada yer alan kodlar kategori sayfasındaki işlemleri gerçekleştirmek içindir.
        category_page=CategoryPage(self.driver)
        category_page.click_second_page()                           #2. sayfaya tıklanır.
        category_page.verify_second_page_clicked("page=2")          #2. sayfada olduğumuz kontrol edilir.                                               
        category_page.click_product()                               #Verilen konumdaki(5.satır 1.sütun) ürüne tıklanır.
        
        #Burada yer alan kodlar ürün sayfasındaki işlemleri gerçekleştirmek içindir.
        product_page=ProductPage(self.driver)
        product_page.verify_product_page("Bu ürün hakkında")        #Ürün sayfasında olduğumuz kontrol edilir. 
        product_page.click_add_to_cart_button()                     #Sepete ekle butonuna tıklanır.
        product_page.verify_product_added_to_cart_and_present_on_cart_page("Sepete Eklendi","Sepet Ara Toplamı:") #Sepete eklendiği ve sepet sayfasında olduğumuz kontrol edilir.
        sleep(3)