import allure
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options  # ИМПОРТ ДЛЯ FIREFOX
from shop_page import CartPage, CheckoutPage, LoginPage, MainPage


@pytest.fixture
def driver():
    """Фикстура запускает Firefox с отключенным менеджером паролей."""
    options = Options()

    # Отключаем встроенный менеджер паролей и предупреждения в Firefox
    options.set_preference("signon.rememberSignons", False)
    options.set_preference("signon.autofillForms", False)
    options.set_preference("signon.generation.enabled", False)

    # Инициализируем «Огненную Лису» с нашими настройками
    browser = webdriver.Firefox(options=options)
    browser.get("https://saucedemo.com")

    yield browser
    browser.quit()


@allure.title("Покупка товаров в интернет-магазине")
@allure.description(
    "Авторизация, добавление трех товаров в корзину "
    "и проверка финальной стоимости в браузере Firefox"
)
@allure.feature("Магазин / Оформление заказа")
@allure.severity(allure.severity_level.BLOCKER)
def test_shop_purchase(driver):
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

    checkout_page.fill_form("Ivan", "Ivanov", "123456")
    total_price = checkout_page.get_total_price()

    msg = f"Неверная итоговая сумма: {total_price}"
    with allure.step("Проверить, что итоговая сумма равна '$58.29'"):
        assert "Total: $58.29" in total_price, msg
