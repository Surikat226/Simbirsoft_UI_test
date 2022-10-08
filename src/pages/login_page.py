from selenium.webdriver.common.by import By
from src.pages.basic_page import BasicPage


class LoginPage(BasicPage):

    EMAIL_DATA_TYPE_BUTTON = (By.XPATH, '//button[@data-type="login"]')
    EMAIL_LOGIN_INPUT = (By.CSS_SELECTOR, '[name="login"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '[id="passp:sign-in"]')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '[id="passp-field-passwd"]')
    AUTH_FORM = (By.CSS_SELECTOR, '[class="passp-auth-content"]')

    # Залогиниться на странице авторизации через форму авторизации
    def login(self, login, password):
        self.is_element_presented(self.EMAIL_DATA_TYPE_BUTTON)

        # Иногда при открытии формы авторизации, по дефолту включён вход по номеру телефона. Переключаемся на
        # вход по email, если эта кнопка незаселекчена
        if self.get_attribute_value(self.EMAIL_DATA_TYPE_BUTTON, 'aria-pressed') == 'false':
            self.click_on_element(self.EMAIL_DATA_TYPE_BUTTON)

        self.click_on_element(self.EMAIL_LOGIN_INPUT)
        self.enter_text(self.EMAIL_LOGIN_INPUT, login)
        self.click_on_element(self.LOGIN_BUTTON)
        self.enter_text(self.PASSWORD_INPUT, password)
        self.click_on_element(self.LOGIN_BUTTON)