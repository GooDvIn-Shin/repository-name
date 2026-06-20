from selenium import webdriver
from calc_page import CalcPage


def test_slow_calculator():
    driver = webdriver.Chrome()
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    )

    calc_page = CalcPage(driver)

    calc_page.set_delay("45")
    calc_page.click_button("7")
    calc_page.click_button("+")
    calc_page.click_button("8")
    calc_page.click_button("=")

    actual_result = calc_page.get_result("15", timeout=46)

    assert actual_result == "15", (
        f"Ожидался результат '15', но на экране "
        f"отобразилось: '{actual_result}'"
    )

    driver.quit()
