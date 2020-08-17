from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_USERNAME = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")

    REG_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REG_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REG_PASSWORD_REPEAT = (By.CSS_SELECTOR, "#id_registration-password2")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ITEM_NAME = (By.CSS_SELECTOR, "h1")
    ITEM_PRICE = (By.CSS_SELECTOR, ".price_color")
    ITEM_ADDED_TO_BASKET_MESSAGE = (By.XPATH, '//div[@id="messages"]/div[1]/div')
    TOTAL_PRICE_OF_BASKET_MESSAGE = (By.XPATH, '//div[@id="messages"]/div[3]/div/p[1]')

