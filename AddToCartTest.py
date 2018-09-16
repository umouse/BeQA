import unittest

from selenium import webdriver


class AddToCartTest(unittest.TestCase):
    WEBSITE = "http://www.rozetka.ua"
    NUMBER_OF_PRODUCTS = 8

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_add_product_to_cart(self):
        self.driver.get(self.WEBSITE)

        popular_links = self.driver.find_elements_by_class_name("popular-g-i-title-link")

        self.assertEqual(len(popular_links), self.NUMBER_OF_PRODUCTS)

        popular_links[0].click()

        details_page_product_name = self.driver.find_element_by_class_name("detail-title").text

        product_price = self.driver.find_element_by_id("price_label").text

        self.driver.find_element_by_name("topurchases").click()

        cart_product_name = self.driver.find_element_by_class_name("cart-i-title-link").text

        cart_product_price = self.driver.find_element_by_name("cost").text

        self.assertEqual(details_page_product_name, cart_product_name)
        self.assertEqual(product_price, cart_product_price)

        self.driver.find_element_by_name("topurchaseskitfromcart").click()

        # wait for kit to be added to cart
        self.driver.find_element_by_css_selector('.cart-kit-total')

        self.driver.find_element_by_css_selector('#cart-popup .cart-amount-plus').click()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
