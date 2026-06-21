from selenium import webdriver
from selenium.webdriver.common.by import By


def test_navigation():
    driver = webdriver.Chrome()
 
    driver.implicitly_wait(5)

    base_url = "https://httpbin.org/"
    driver.get(base_url)

    forms_link = driver.find_element(By.CSS_SELECTOR, "a[href='/forms/post']")
    forms_link.click()

    assert driver.current_url.endswith("/forms/post"), f"Ожидался URL с /forms/post, но получили {driver.current_url}"

    driver.back()

    assert driver.current_url == base_url, f"Ожидался возврат на {base_url}, но текущий URL: {driver.current_url}"

    driver.quit()
