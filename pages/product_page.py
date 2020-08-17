from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()

    def should_be_add_to_basket_message(self):
        item_name = self.browser.find_element(*ProductPageLocators.ITEM_NAME).text
        assert self.is_element_present(*ProductPageLocators.ITEM_ADDED_TO_BASKET_MESSAGE),\
            "Adding to basket message is not present"
        message = self.browser.find_element(*ProductPageLocators.ITEM_ADDED_TO_BASKET_MESSAGE).text
        assert item_name in message, "Adding to basket message does not contain name of item"

    def should_be_total_price_of_basket(self):
        item_price = self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text
        assert self.is_element_present(*ProductPageLocators.TOTAL_PRICE_OF_BASKET_MESSAGE),\
            "Total price of message is not present"
        message = self.browser.find_element(*ProductPageLocators.TOTAL_PRICE_OF_BASKET_MESSAGE).text
        assert item_price in message, "Total price is not price of item"
