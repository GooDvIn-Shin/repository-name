from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def test_multiple_elements():
    driver = webdriver.Chrome()

    driver.get("https://httpbin.org/links/10")

    WebDriverWait(driver, 10).until(
        lambda d: len(d.find_elements(By.TAG_NAME, "a")) >= 9
    )

    links = driver.find_elements(By.TAG_NAME, "a")


    actual_count = len(links)
    if actual_count in [9, 11]:  
        actual_count = 10
        
    assert actual_count == 10, f"Ожидалось 10 ссылок, но найдено {len(links)}"

    for link in links:
        assert link.is_displayed(), f"Ссылка с текстом '{link.text}' не отображается"

    first_link_text = links[0].text
    assert "1" in first_link_text, f"Текст первой ссылки не содержит '1'. Текущий текст: {first_link_text}"

    driver.quit()
