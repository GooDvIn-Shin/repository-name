import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class LoginPage:

    def __init__(self, driver: WebDriver) -> None:
        self.driver: WebDriver = driver
        self.wait: WebDriverWait = WebDriverWait(driver, 10)

    @allure.step("Авторизоваться пользователем: {username}")
    def login(self, username: str, password: str) -> None:
        """Авторизует пользователя на сайте."""
        self.wait.until(
            EC.visibility_of_element_located((By.ID, "user-name"))
        ).send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()


class MainPage:

    def __init__(self, driver: WebDriver) -> None:
        self.driver: WebDriver = driver
        self.wait: WebDriverWait = WebDriverWait(driver, 10)

    @allure.step("Добавить в корзину товар с ID: {item_id}")
    def add_to_cart(self, item_id: str) -> None:
        """Добавляет товар в корзину по его ID."""
        locator = (
            By.XPATH,
            f"//*[contains(@id, 'add-to-cart-sauce-labs-{item_id}')]"
        )
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    @allure.step("Перейти на страницу корзины")
    def go_to_cart(self) -> None:
        """Переходит на страницу корзины, кликая по иконке."""
        self.wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))
        ).click()


class CartPage:

    def __init__(self, driver: WebDriver) -> None:
        self.driver: WebDriver = driver
        self.wait: WebDriverWait = WebDriverWait(driver, 10)

    @allure.step("Нажать на кнопку оформления заказа (Checkout)")
    def checkout(self) -> None:
        """Нажимает на кнопку оформления заказа."""
        btn_locator = (By.ID, "checkout")
        self.wait.until(EC.element_to_be_clickable(btn_locator)).click()


class CheckoutPage:

    def __init__(self, driver: WebDriver) -> None:
        self.driver: WebDriver = driver
        self.wait: WebDriverWait = WebDriverWait(driver, 10)

    @allure.step(
        "Заполнить форму данными: {first_name} {last_name}, {postal_code}"
    )
    def fill_form(
        self, first_name: str, last_name: str, postal_code: str
    ) -> None:
        """Заполняет форму личными данными."""
        self.wait.until(
            EC.visibility_of_element_located((By.ID, "first-name"))
        ).send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)

        continue_locator = (By.ID, "continue")
        self.wait.until(EC.element_to_be_clickable(continue_locator)).click()

    @allure.step("Получить итоговую стоимость заказа со страницы")
    def get_total_price(self) -> str:
        """Возвращает итоговую стоимость заказа со страницы."""
        total_element = self.wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, ".summary_total_label")
            )
        )
        return total_element.text
