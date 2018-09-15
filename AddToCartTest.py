import unittest

from selenium import webdriver


class AddToCartTest(unittest.TestCase):
    WEBSITE = "http://www.rozetka.ua"
    NUMBER_OF_PRODUCTS = 8

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(4)

    def test_add_product_to_cart(self):
        self.driver.get(self.WEBSITE)

        popular_links = self.driver.find_elements_by_class_name("popular-g-i-title-link")

        self.assertEqual(len(popular_links), self.NUMBER_OF_PRODUCTS)

        popular_link = popular_links[0]
        popular_link.click()

        product_name = self.driver.find_element_by_class_name("detail-title")
        details_page_product_name = product_name.text

        price = self.driver.find_element_by_id("price_label")
        product_price = price.text

        submit_button = self.driver.find_element_by_name("topurchases")
        submit_button.click()

        product_name = self.driver.find_element_by_class_name("cart-i-title-link")
        cart_product_name = product_name.text

        price = self.driver.find_element_by_name("cost")
        cart_product_price = price.text

        self.assertEqual(details_page_product_name, cart_product_name)
        self.assertEqual(product_price, cart_product_price)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
