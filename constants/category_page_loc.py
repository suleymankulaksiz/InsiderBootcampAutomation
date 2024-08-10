from selenium.webdriver.common.by import By

SECOND_PAGE             = (By.CSS_SELECTOR,"a[aria-label='2 sayfasına git']")
SECOND_PAGE_ASSERT      = (By.CSS_SELECTOR,"[class='s-pagination-item s-pagination-selected']")
VERIFY_SECOND_PAGE      = (By.CSS_SELECTOR, "[class='s-pagination-item s-pagination-selected']")
ALL_PRODUCT             = (By.XPATH, "//div[@data-component-type='s-search-result']")

sponsored_products_text = "puis-label-popover puis-sponsored-label-text"