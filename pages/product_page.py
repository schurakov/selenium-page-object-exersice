from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def should_be_correct_price_in_basket(self):
        expected_price = self.get_product_price()
        price_in_basket = self.browser.find_element(*ProductPageLocators.BASKET_IN_RIGHT_CORNER)
        assert expected_price in price_in_basket.text, "Unexpected price in basket"

    def should_be_correct_product_name_in_notification(self):
        expected_name = self.get_product_name()
        notification = self.browser.find_element(*ProductPageLocators.ADDED_TO_BASKET_ALERT)
        assert expected_name in notification.text, "Unexpected product name in add to basket notification"

    def get_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_MAIN_PRISE)
        return product_price.text

    def get_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_MAIN_NAME)
        return product_name.text
