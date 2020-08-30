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
        print(expected_price, '\n', price_in_basket.text)

    def should_be_correct_add_to_basket_notification(self):
        expected_notification = self.get_product_name() + " has been added to your basket."
        notification = self.browser.find_element(*ProductPageLocators.ADDED_TO_BASKET_ALERT)
        print(expected_notification, '\n', notification.text)
        assert expected_notification == notification.text, "Unexpected product name in add to basket notification"


    def get_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_MAIN_PRISE)
        return product_price.text

    def get_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_MAIN_NAME)
        return product_name.text

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ADDED_TO_BASKET_ALERT), \
            "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.ADDED_TO_BASKET_ALERT), \
            "Success message is not disappeared, but should be"
