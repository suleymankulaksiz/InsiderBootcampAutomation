import pytest
from pages.home_page import *
from pages.category_page import *
from pages.product_page import *
import allure

@pytest.mark.usefixtures("setup")
class TestProcess():
    @allure.title('Ürün adı aratılarak sepete ekleme ve tekrar anasayfaya dönme işlemleri test edilecektir.')
    def test_product_addition_to_cart_on_amazon(self):
        #Burada yer alan kodlar anasayfadaki işlemleri gerçekleştirmek içindir.
        home_page= HomePage(self.driver)
        home_page.accept_cookies()                                                                                #Çerez kabul edilir.
        home_page.verify_homepage_opened("https://www.amazon.com.tr/")                                            #Anasayfa'nın açıldığı kontrol edilir.
        home_page.click_the_searchbox_and_enter_text("Samsung")                                                   #Arama kutsuna tıklanır ve Samsung ifadesi girilir.
        home_page.verify_searchbox_text("Samsung")                                                                #Searchbox alanına, doğru verinin girildiği kontrol edilir.
        home_page.click_search_icon()                                                                             #Arama ikonuna tıklanır.
        home_page.verify_results_samsung("Amazon.com.tr : Samsung")                                               #Samsung için sonuç bulduğu kontrol edilir.
        #Burada yer alan kodlar kategori sayfasındaki işlemleri gerçekleştirmek içindir.
        category_page=CategoryPage(self.driver)
        category_page.click_second_page()                                                                         #2. sayfaya tıklanır.
        category_page.verify_second_page_clicked("page=2")                                                        #2. sayfada olduğumuz kontrol edilir.                                               
        category_page.click_product_from_list(20)                                                                 #Verilen konumdaki(5.satır 1.sütun) ürüne tıklanır.
        #Burada yer alan kodlar ürün sayfasındaki işlemleri gerçekleştirmek içindir.
        product_page=ProductPage(self.driver)
        product_page.verify_product_page("Bu ürün hakkında")                                                      #Ürün sayfasında olduğumuz kontrol edilir. 
        product_page.click_add_to_cart_button()                                                                   #Sepete ekle butonuna tıklanır.
        product_page.verify_product_added_to_cart_and_present_on_cart_page("Sepete Eklendi","Sepet Ara Toplamı:") #Sepete eklendiği ve sepet sayfasında olduğumuz kontrol edilir.
        product_page.click_amazon_logo()                                                                          #Sol üst köşedeki Amazon logosuna tıklanır.
        product_page.verify_returned_to_homepage("amazon.com.tr/ref=nav_logo")                                    #Anasayfa'ya dönüldüğü kontrol edilir.