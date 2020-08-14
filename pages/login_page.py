from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        login_check = "login"
        assert login_check in self.browser.current_url, "URL don't have 'login' substring"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_USERNAME),\
            "Username input is not presented in login form"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD),\
            "Password input is not presented in login form"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REG_EMAIL),\
            "Username input is not presented in registration form"
        assert self.is_element_present(*LoginPageLocators.REG_PASSWORD),\
            "Password input is not presented in registration form"
        assert self.is_element_present(*LoginPageLocators.REG_PASSWORD_REPEAT),\
            "Password repeat input is not presented in registration form"
