from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_01_form():
    driver = webdriver.Edge()
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
    )

    wait = WebDriverWait(driver, 10)

    # Данные для заполнения формы (согласно таблице)
    form_data = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "e-mail": "test@skypro.com",
        "phone": "+7985899998787",
        "city": "Москва",
        "country": "Россия",
        "job-position": "QA",
        "company": "SkyPro"
    }

    for field_name, value in form_data.items():
        element = wait.until(
            EC.visibility_of_element_located((By.NAME, field_name))
        )
        element.send_keys(value)

    submit_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
    )
    submit_button.click()

    zip_code_element = wait.until(
        EC.visibility_of_element_located((By.ID, "zip-code"))
    )

    zip_class = zip_code_element.get_attribute("class")
    assert "alert-danger" in zip_class, (
        f"Поле Zip code должно быть красным, но его класс: {zip_class}"
    )

    green_fields = [
        "first-name", "last-name", "address", "e-mail",
        "phone", "city", "country", "job-position", "company"
    ]

    for field_id in green_fields:
        field_element = driver.find_element(By.ID, field_id)
        field_class = field_element.get_attribute("class")
        assert "alert-success" in field_class, (
            f"Поле {field_id} должно быть зеленым, но его класс: {field_class}"
        )

    driver.quit()
