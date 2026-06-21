from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CalcPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def set_delay(self, seconds: str):
        """Очищает поле задержки и вводит новое значение."""
        delay_input = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#delay"))
        )
        delay_input.clear()
        delay_input.send_keys(seconds)

    def click_button(self, text: str):
        """Находит кнопку калькулятора по её тексту и кликает."""
        button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//span[text()='{text}']"))
        )
        button.click()

    def get_result(self, expected_text: str, timeout: int) -> str:
        """Ожидает появление текста на экране калькулятора и возвращает его."""
        long_wait = WebDriverWait(self.driver, timeout)
        screen_locator = (By.CSS_SELECTOR, ".screen")

        long_wait.until(
            EC.text_to_be_present_in_element(screen_locator, expected_text)
        )

        return self.driver.find_element(*screen_locator).text
