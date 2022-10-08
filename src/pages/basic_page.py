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

    # Нажать на ENTER на клавиатуре
    def press_enter(self, locator, timeout=5):
        WDW(self.browser, timeout).until(EC.visibility_of_element_located(locator),
                                         message=f"Не удалось найти локатор {locator}!").send_keys(Keys.ENTER)

    # Ввести текст в поле
    def enter_text(self, locator, text, timeout=5):
        WDW(self.browser, timeout).until(EC.presence_of_element_located(locator),
                                         message=f"Не удалось найти локатор {locator}!").send_keys(text)

    # Пройтись по списку всех элементов с одинаковыми локаторами и найти среди них элемент с определённым текстом.
    # Метод возвращает найденный элемент, с которым можно взаимодействовать в дальнейшем
    def find_element_with_specific_text(self, locator, text, timeout=5):
        elements = WDW(self.browser, timeout).until(EC.visibility_of_all_elements_located(locator),
                                                    message=f"Не удалось найти локатор {locator}!")
        for element in elements:
            if element.text == text:
                return element

    # Првоерить наличие элемента в DOM
    def is_element_presented(self, locator, timeout=5):
        element = WDW(self.browser, timeout).until(EC.presence_of_element_located(locator),
                                                   message=f"Не удалось найти локатор {locator}!")
        return bool(element)

    # Проверить, что элемент отображается на странице
    def is_element_visible(self, locator, timeout=5):
        element = WDW(self.browser, timeout).until(EC.visibility_of_element_located(locator),
                                                   message=f"Не удалось найти локатор {locator}!")
        return bool(element)

    # Проверить, что элемент отсутствует в DOM
    def is_element_not_presented(self, locator, timeout=5):
        element = WDW(self.browser, timeout).until_not(EC.presence_of_element_located(locator),
                                                       message=f"Не удалось найти локатор {locator}!")
        return bool(element)

    # Проверить, что элемент кликабелен
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

    # Получить значение определённого атрибута элемента
    def get_attribute_value(self, locator, attribute_name, timeout=5):
        element = WDW(self.browser, timeout).until(EC.presence_of_element_located(locator),
                                                   message=f"Не удалось найти локатор {locator}!")
        attribute_value = element.get_attribute(attribute_name)
        return attribute_value

    # Загрузить файл
    def upload_file(self, locator, file_path, timeout=5):
        element = WDW(self.browser, timeout).until(EC.visibility_of_element_located(locator),
                                                   message=f"Не удалось найти локатор {locator}!")
        element.send_keys(file_path)

    # Открыть локальный файл и получить его содержимое. На вход подаётся путь к файлу
    def get_local_file_content(self, file_path):
        with open(file_path, "rt", encoding="utf-8") as file:
            content = file.read().rstrip()
            return content

    # Получить текст элемента
    def get_element_text(self, locator, timeout=5):
        element = WDW(self.browser, timeout).until(EC.visibility_of_element_located(locator),
                                                   message=f"Не удалось найти локатор {locator}!")
        return element.text