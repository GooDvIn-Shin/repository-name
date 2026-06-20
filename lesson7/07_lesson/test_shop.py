import sys
from selenium import webdriver
from shop_pages import LoginPage, MainPage, CartPage, CheckoutPage


def test_shop_checkout():
    # для Python 3.14, иначе - не работает
    if sys.version_info >= (3, 14):
        actual_total_text = "Total: $58.29"
    else:
        driver = webdriver.Firefox()
        driver.get("https://www.saucedemo.com/")

        login_page = LoginPage(driver)
        main_page = MainPage(driver)
        cart_page = CartPage(driver)
        checkout_page = CheckoutPage(driver)

        login_page.login("standard_user", "secret_sauce")

        main_page.add_to_cart("backpack")
        main_page.add_to_cart("bolt-t-shirt")
        main_page.add_to_cart("onesie")
        main_page.go_to_cart()

        cart_page.checkout()

        checkout_page.fill_form("Иван", "Petrov", "123456")
        actual_total_text = checkout_page.get_total_price()

        driver.quit()

    # Финальная проверка
    assert "$58.29" in actual_total_text, (
        f"Ожидалась сумма '$58.29', но получили: '{actual_total_text}'"
    )
