import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utilities.BaseClass import BaseClass


class TestOne(BaseClass):
    def test_header(self):
        log = self.getLogger()
        menu_items = self.driver.find_elements_by_css_selector(".menu-main-container ul li a")
        for item in menu_items:
            print(item.text)
        log.info("Menu Items: " +str(len(menu_items)))

    def test_homepageProducts(self):
        log = self.getLogger()
        self.scrollEndPage()  # scroll to end of the page because of lazyloading at the products div

        self.verifyLinkPresence("Baby short sleeve one piece")
        products_items = self.driver.find_elements_by_css_selector(".content-product .product-details h2 a")
        for product in products_items:
            print(product.text)
        log.info("Product Items: "+ str(len(products_items)))

    def test_footer(self):
        log = self.getLogger()

        cookies_link = self.driver.find_element_by_link_text("Cookies1").text
        privacy_link = self.driver.find_element_by_link_text("Privacy Policies").text
        terms_link = self.driver.find_element_by_link_text("Terms & Conditions").text


