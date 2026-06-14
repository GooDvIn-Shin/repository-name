from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_02_calc():
    driver = webdriver.Chrome()
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    )

    short_wait = WebDriverWait(driver, 10)

    delay_input = short_wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#delay"))
    )
    delay_input.clear()
    delay_input.send_keys("45")

    btn_7 = short_wait.until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='7']"))
    )
    btn_7.click()

    btn_plus = short_wait.until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='+']"))
    )
    btn_plus.click()

    btn_8 = short_wait.until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='8']"))
    )
    btn_8.click()

    btn_equal = short_wait.until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='=']"))
    )
    btn_equal.click()

    long_wait = WebDriverWait(driver, 45)

    long_wait.until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
    )

    actual_result = driver.find_element(By.CSS_SELECTOR, ".screen").text
    assert actual_result == "15", (
        f"Ожидался результат '15', но на экране "
        f"отобразилось: '{actual_result}'"
    )

    driver.quit()
