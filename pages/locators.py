from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    PAGE_URL = ""
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_FORM_EMAIL = (By.CSS_SELECTOR, "[name='registration-email']")
    REGISTRATION_FORM_PASS = (By.CSS_SELECTOR, "[name='registration-password1']")
    REGISTRATION_FORM_CONFIRM_PASS = (By.CSS_SELECTOR, "[name='registration-password2']")
    LOGIN_FORM_EMAIL = (By.CSS_SELECTOR, "[name='login-username']")
    LOGIN_FORM_PASS = (By.CSS_SELECTOR, "[name='login-password']")
