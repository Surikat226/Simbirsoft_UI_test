import time
from src.pages.basic_page import BasicPage
from src.data.main_data import MainData
from selenium.webdriver.common.by import By

test_data = MainData()


class YandexDiskPage(BasicPage):

    CREATE_BUTTON = (By.XPATH, '//button//span[text()="Создать"]/..')

    # Типы файлов в попапе создания файлов
    CREATE_FOLDER_POPUP = (By.XPATH, '//button//span[text()="Папку"]/..')
    CREATE_TEXT_FILE_POPUP = (By.XPATH, '//button//span[text()="Текстовый документ"]/..')
    # /Типы файлов в попапе создания файлов
    FILE_NAME_MODAL_WINDOW = (By.XPATH, '//form[contains(@class, "dialog")]//input')
    SAVE_BUTTON_MODAL_WINDOW = (By.XPATH, '//div[contains(@class, "confirmation")]/button/span[text()="Сохранить"]/..')
    CREATE_BUTTON_MODAL_WINDOW = (By.XPATH, '//div[contains(@class, "confirmation")]/button/span[text()="Создать"]/..')
    LAST_ITEM = (By.XPATH, '(//div[contains(@class, "listing-item__title")])[last()]')
    # Выбранный элемент после клика по нему
    SELECTED_ITEM = (By.XPATH, '//div[contains(@class, "listing-item") and @aria-selected="true"]')
    # /Выбранный элемент после клика по нему
    ACCOUNT_ICON_LINK = (By.CSS_SELECTOR, '[aria-label="Аккаунт"]')
    LOGOUT_FROM_ACCOUNT_LINK = (By.CSS_SELECTOR, '[aria-label="Выйти из аккаунта"]')
    ULOAD_FILES_INPUT = (By.CSS_SELECTOR, '[type="file"]')
    OPENED_FILE_TEXT = (By.CSS_SELECTOR, 'p.mg1')
    CANCEL_HIGHLIGHT_BUTTON = (By.CSS_SELECTOR, '[aria-label="Отменить выделение"]')

    # Создать файл. В качестве аргументов передаются тип создаваемого файла и его имя
    def create_file(self, file_type, file_name):
        self.click_on_element(self.CREATE_BUTTON)

        if file_type == 'Папку':
            self.click_on_element(self.CREATE_FOLDER_POPUP)
        elif file_type == 'Текстовый документ':
            self.click_on_element(self.CREATE_TEXT_FILE_POPUP)

        # Ввод названия файла/папки
        time.sleep(1.5)
        self.enter_text(self.FILE_NAME_MODAL_WINDOW, file_name)

        # Клик по кнопке сохранения файла/папки. Текст кнопки сохранения варьируется в зависимости от типа файла,
        # поэтому было сделано условие нажатия
        if file_type == 'Папку':
            self.click_on_element(self.SAVE_BUTTON_MODAL_WINDOW)
        elif file_type == 'Текстовый документ':
            self.click_on_element(self.CREATE_BUTTON_MODAL_WINDOW)

    # Найти айтем (файл/папку) в диске по имени. Также, можно дополнительно ввести формат файла типа .docx, .txt и т.д.
    def find_item_by_name(self, item_name, file_format=''):

        item = (By.XPATH,
               f'//div[@class="client-listing"]//div[contains(@class, "listing-item__title") and @aria-label="{item_name}{file_format}"]/..')
               # f'//div[contains(@class, "listing-item__title") and @aria-label="{item_name}{file_format}"]/..')
        return item

    def logout_from_yadidisk(self):
        self.click_on_element(self.ACCOUNT_ICON_LINK)
        self.click_on_element(self.LOGOUT_FROM_ACCOUNT_LINK)

    # ========================================================
    # ПРОВЕРКИ
    # ========================================================

    # Проверка имени последнего созданного файла на соответствие имени на входе функции
    def check_file_names(self, comparable_file_name):
        assert (self.get_attribute_value(self.LAST_ITEM, 'aria-label') == comparable_file_name), \
            "Файл с таким именем не был найден"

    # Проверка текста в открытом файле с текстом, поданным на вход функции
    def check_opened_file_text(self, comparable_file_text):
        assert (self.get_element_text(self.OPENED_FILE_TEXT) == comparable_file_text), \
            "Текст файла в браузере не совпадает с текстом для сравнения"