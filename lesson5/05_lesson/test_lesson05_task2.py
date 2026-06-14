import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submission():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)

    start_url = "https://httpbin.org/forms/post"
    driver.get(start_url)

    name_input = driver.find_element(By.NAME, "custname")

    name_input.send_keys("Студент-Тестировщик")

    submit_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Submit')]")
    submit_button.click()

    time.sleep(2)

    assert driver.current_url != start_url, f"URL не изменился и остался {start_url}"
    assert driver.current_url.endswith("/post"), f"Ожидался URL с /post на конце, но получили {driver.current_url}"

    driver.quit()
