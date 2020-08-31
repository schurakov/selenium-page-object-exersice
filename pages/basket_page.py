from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.SOME_PRODUCT_IN_BASKET), \
            "Some product in basket, but should not be"

    def should_be_text_about_empty_basket(self):
        expected_text = "Your basket is empty. Continue shopping"
        actual_text = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_TEXT)
        assert actual_text.text == expected_text, f"Unexpected empty basket text: {actual_text.text}. Expected: {expected_text}"
