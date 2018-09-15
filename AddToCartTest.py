import unittest

from selenium import webdriver


class AddToCartTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(4)

    def test_add_product_to_cart(self):
        self.driver.get("http://www.rozetka.ua")

        popular_link = self.driver.find_element_by_class_name("popular-g-i-title-link")
        popular_link.click()

        product_name = self.driver.find_element_by_class_name("detail-title")
        details_page_product_name = product_name.text

        submit_button = self.driver.find_element_by_name("topurchases")
        submit_button.click()

        product_name = self.driver.find_element_by_class_name("cart-i-title-link")
        cart_product_name = product_name.text

        self.assertEqual(details_page_product_name, cart_product_name)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
