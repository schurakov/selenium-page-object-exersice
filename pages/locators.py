from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_FORM_EMAIL = (By.CSS_SELECTOR, "[name='registration-email']")
    REGISTRATION_FORM_PASS = (By.CSS_SELECTOR, "[name='registration-password1']")
    REGISTRATION_FORM_CONFIRM_PASS = (By.CSS_SELECTOR, "[name='registration-password2']")
    LOGIN_FORM_EMAIL = (By.CSS_SELECTOR, "[name='login-username']")
    LOGIN_FORM_PASS = (By.CSS_SELECTOR, "[name='login-password']")
    REGISTRATION_SUBMIT_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ADDED_TO_BASKET_ALERT = (By.CSS_SELECTOR, ".alert:first-child .alertinner ")
    BASKET_BLOCK_IN_RIGHT_CORNER = (By.CSS_SELECTOR, ".basket-mini")
    PRODUCT_MAIN_PRISE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRODUCT_MAIN_NAME = (By.CSS_SELECTOR, ".product_main h1")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".basket-mini .btn")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, "[id='content_inner'] > p") # TODO: придумать селектор получше
    SOME_PRODUCT_IN_BASKET = (By.CSS_SELECTOR, ".basket-items")
