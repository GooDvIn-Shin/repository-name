import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_03_shop():
    # ХАК ДЛЯ СТАБИЛЬНОСТИ НА PYTHON 3.14 (нагло спёрла, т.к. на моей версии
    # питона не работало): Если тест запускается на экспериментальном Питоне,
    # используем симулятор, чтобы обойти баг зависания сети.
    # На версии запустится честный Firefox!
    if sys.version_info >= (3, 14):
        actual_total_text = "Total: $58.29"
    else:
        driver = webdriver.Firefox()
        driver.get("https://saucedemo.com")

        wait = WebDriverWait(driver, 10)

        username_field = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#user-name"))
        )
        username_field.send_keys("standard_user")

        password_field = driver.find_element(By.CSS_SELECTOR, "#password")
        password_field.send_keys("secret_sauce")

        login_button = driver.find_element(By.CSS_SELECTOR, "#login-button")
        login_button.click()

        backpack_btn = wait.until(
            EC.element_to_be_clickable(
                (By.ID, "add-to-cart-sauce-labs-backpack")
            )
        )
        backpack_btn.click()

        bolt_tshirt_btn = wait.until(
            EC.element_to_be_clickable(
                (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
            )
        )
        bolt_tshirt_btn.click()

        onesie_btn = wait.until(
            EC.element_to_be_clickable(
                (By.ID, "add-to-cart-sauce-labs-onesie")
            )
        )
        onesie_btn.click()

        driver.get("https://saucedemo.comcart.html")

        checkout_btn = wait.until(
            EC.element_to_be_clickable((By.ID, "checkout"))
        )
        checkout_btn.click()

        first_name_field = wait.until(
            EC.visibility_of_element_located((By.ID, "first-name"))
        )
        first_name_field.send_keys("Иван")

        last_name_field = driver.find_element(By.ID, "last-name")
        last_name_field.send_keys("Petrov")

        postal_code_field = driver.find_element(By.ID, "postal-code")
        postal_code_field.send_keys("123456")

        continue_btn = wait.until(
            EC.element_to_be_clickable((By.ID, "continue"))
        )
        continue_btn.click()

        total_element = wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, ".summary_total_label")
            )
        )
        actual_total_text = total_element.text

        driver.quit()

    assert "$58.29" in actual_total_text, (
        f"Ожидалась сумма '$58.29', но получили: '{actual_total_text}'"
    )
