from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dynamic_loading():
    driver = webdriver.Chrome()

    # 1. Откройте страницу https://the-internet.herokuapp.com/dynamic_loading/2
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

    # Настраиваем явное ожидание максимум на 15 секунд (сайт бывает тупит)
    wait = WebDriverWait(driver, 15)

    # 2. Найдите и нажмите на кнопку "Start"
    # Находим кнопку через CSS-селектор внутри блока #start
    start_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#start button"))
    )
    start_button.click()

    # 3. Дождитесь появления текста "Hello World!"
    # Ждем, пока элемент с id="finish" и текстом станет видимым на экране
    finish_text_element = wait.until(
        EC.visibility_of_element_located((By.ID, "finish"))
    )

    # 4. Сделайте скриншот страницы
    # Скриншот сохранится в ту же папку, где лежит этот файл теста
    driver.save_screenshot("screenshot_task1.png")

    # 5. Проверьте, что появившийся текст равен "Hello World!"
    actual_text = finish_text_element.text
    assert actual_text == "Hello World!", (
        f"Ожидался текст 'Hello World!', но получили '{actual_text}'"
    )

    driver.quit()
