import allure
import pytest
from selenium import webdriver
from calc_page import CalcPage


@pytest.fixture
def driver():
    """Фикстура запускает браузер перед тестом."""
    browser = webdriver.Chrome()
    url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"  # noqa: E501
    browser.get(url)
    yield browser
    browser.quit()


@allure.title("Проверка работы калькулятора с задержкой")
@allure.description(
    "Тест устанавливает задержку, складывает 7 и 8, "
    "затем проверяет результат 15"
)
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_calculator(driver):
    calc = CalcPage(driver)

    calc.set_delay("4")
    calc.click_button("7")
    calc.click_button("+")
    calc.click_button("8")
    calc.click_button("=")

    result = calc.get_result("15", 15)

    msg = f"Ожидалось число 15, но калькулятор показал: {result}"
    with allure.step("Проверить, что на экране результат '15'"):
        assert result == "15", msg
