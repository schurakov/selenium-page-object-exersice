from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def should_be_correct_price_in_basket(self):
        price_in_basket = self.browser.find_element(*ProductPageLocators.BASKET_IN_RIGHT_CORNER)
        assert "9.99" in price_in_basket.text, "Unexpected price in basket"

    def should_be_correct_product_name_in_notification(self):
        notification = self.browser.find_element(*ProductPageLocators.ADDED_TO_BASKET_ALERT)
        assert "The shellcoder's handbook" in notification.text, "Unexpected product name in add to basket notification"
