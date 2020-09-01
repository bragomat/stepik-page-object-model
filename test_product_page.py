import pytest
from pages.product_page import ProductPage


# @pytest.mark.parametrize('url', ["?promo=offer0",
#                                  "?promo=offer1",
#                                  "?promo=offer2",
#                                  "?promo=offer3",
#                                  "?promo=offer4",
#                                  "?promo=offer5",
#                                  "?promo=offer6",
#                                  pytest.param("?promo=offer7", marks=pytest.mark.xfail),
#                                  "?promo=offer8",
#                                  "?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, url):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/" + url
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_add_to_basket_message()
    page.should_be_total_price_of_basket()


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_not_add_to_basket_message()


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_not_add_to_basket_message()


def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_disappeared_add_to_basket_message()

