import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AddToCartTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()

    def test_add_product_to_cart(self):
        self.driver.get("http://www.google.com")

        website_name = "rozetka"
        wait = WebDriverWait(self.driver, 10)

        search_field = wait.until(EC.presence_of_element_located((By.NAME, "q")))
        search_field.send_keys(website_name)
        search_field.submit()

        rozetka_link = wait.until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "ROZETKA™")))
        rozetka_link.click()

        popular_link = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "popular-g-i-title-link")))
        popular_link.click()

        product_name = self.driver.find_element_by_class_name("detail-title")
        details_page_product_name = product_name.text

        submit_button = wait.until(EC.presence_of_element_located((By.NAME,"topurchases")))
        submit_button.click()

        product_name = wait.until(EC.presence_of_element_located((By.CLASS_NAME,"cart-i-title-link")))
        cart_product_name = product_name.text

        self.assertEqual(details_page_product_name,cart_product_name)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
