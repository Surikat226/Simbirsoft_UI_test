from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys


class BasicPage:

    # Базовые локаторы
    DZEN_LOGIN_BUTTON = (By.XPATH, '//span[contains(@class, "zen-ui-button") and text()="Войти"]')

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    # Открыть браузер и страницу
    def open(self):
        self.browser.get(self.url)

    # Кликнуть по элементу
    def click_on_element(self, locator, timeout=5):
        WDW(self.browser, timeout).until(EC.element_to_be_clickable(locator),
                                         message=f"Не удалось найти локатор {locator}!").click()

    def press_enter(self, locator, timeout=5):
        WDW(self.browser, timeout).until(EC.visibility_of_element_located(locator),
                                         message=f"Не удалось найти локатор {locator}!").send_keys(Keys.ENTER)

    # Ввести текст в поле
    def enter_text(self, locator, text, timeout=5):
        WDW(self.browser, timeout).until(EC.presence_of_element_located(locator),
                                         message=f"Не удалось найти локатор {locator}!").send_keys(text)

    def is_element_presented(self, locator, timeout=5):
        element = WDW(self.browser, timeout).until(EC.presence_of_element_located(locator),
                                                   message=f"Не удалось найти локатор {locator}!")
        return bool(element)

    def is_element_not_presented(self, locator, timeout=5):
        element = WDW(self.browser, timeout).until_not(EC.presence_of_element_located(locator),
                                                       message=f"Не удалось найти локатор {locator}!")
        return bool(element)

    def is_element_clickable(self, locator, timeout=5):
        element = WDW(self.browser, timeout).until(EC.element_to_be_clickable(locator),
                                                   message=f"Cant find element by locator {locator}!")
        return bool(element)

    # Переключиться на вкладку с определённым индексом. Метод принимает индекс вкладки, на которую нужно перейти
    def switch_to_another_window(self, window_index):
        self.browser.switch_to.window(self.browser.window_handles[window_index])

    # Закрыть вкладку с определённым индексом. Метод принимает индекс вкладки, которую необходимо закрыть
    def close_specific_window(self, window_index):
        window = self.browser.window_handles[window_index]
        self.browser.switch_to.window(window)
        self.browser.close()

    def get_attribute_value(self, locator, attribute_name, timeout=5):
        element = WDW(self.browser, timeout).until(EC.presence_of_element_located(locator),
                                                   message=f"Не удалось найти локатор {locator}!")
        attribute_value = element.get_attribute(attribute_name)
        return attribute_value

    def upload_file(self, locator, file_path, timeout=5):
        element = WDW(self.browser, timeout).until(EC.visibility_of_element_located(locator),
                                                   message=f"Не удалось найти локатор {locator}!")
        element.send_keys(file_path)

    def get_local_file_content(self, file_path):
        with open(file_path, "rt", encoding="utf-8") as file:
            content = file.read().rstrip()
            return content

    def get_element_text(self, locator, timeout=5):
        element = WDW(self.browser, timeout).until(EC.visibility_of_element_located(locator),
                                                   message=f"Не удалось найти локатор {locator}!")
        return element.text