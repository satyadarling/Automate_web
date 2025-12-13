import time

import pytest
from tests.login_page import LoginPage
from tests.home_page import HomePage
from tests.product_page import ProductPage
from tests.cart_page import CartPage
from tests.sinup import SinUp


def test_e2e(setup):
    driver = setup

    home = HomePage(driver)
    home.go_to_login()

    login = LoginPage(driver)
    log=login.login("satya1@gmail.com", "satya@")
    if not log:

        sinup=SinUp(driver)
        sinup.Sinup("satya1","satya1@gmail.com")
        sinup.nextstep("satya@","26","4","1995",'nani','all','bhuvi','India','ap','bhu','56789','9848022338')
        time.sleep(10)
        login = LoginPage(driver)
        log = login.login("satya1@gmail.com", "satya@")

    home.search_product("Tshirt")

    product = ProductPage(driver)
    product.add_first_product_to_cart()

    cart = CartPage(driver)
    cart.proceed_to_checkout()

    home.logout()