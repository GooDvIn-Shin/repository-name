from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def login(self, username, password):
        """Авторизует пользователя на сайте."""
        self.wait.until(
            EC.visibility_of_element_located((By.ID, "user-name"))
        ).send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()


class MainPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_to_cart(self, item_id: str):
        """Добавляет товар в корзину по его ID."""
        self.wait.until(
            EC.element_to_be_clickable(
                (By.ID, f"add-to-cart-sauce-labs-{item_id}")
            )
        ).click()

    def go_to_cart(self):
        """Переходит на страницу корзины."""
        self.driver.get("https://saucedemo.com")


class CartPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def checkout(self):
        """Нажимает на кнопку оформления заказа."""
        btn_locator = (By.ID, "checkout")
        self.wait.until(
            EC.element_to_be_clickable(btn_locator)
        ).click()


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_form(self, first_name, last_name, postal_code):
        """Заполняет форму личными данными."""
        self.wait.until(
            EC.visibility_of_element_located((By.ID, "first-name"))
        ).send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)

        continue_locator = (By.ID, "continue")
        self.wait.until(
            EC.element_to_be_clickable(continue_locator)
        ).click()

    def get_total_price(self) -> str:
        """Возвращает итоговую стоимость заказа со страницы."""
        total_element = self.wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, ".summary_total_label")
            )
        )
        return total_element.text
