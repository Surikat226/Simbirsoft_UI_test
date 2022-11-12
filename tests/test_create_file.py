from src.pages.login_page import LoginPage
from src.pages.yandex_disk_page import YandexDiskPage
from src.data.main_data import MainData

# Экземпляр класса нужен для того, чтобы не прописывать обращение напрямую к классу и его атрибутам на случай,
# если в нём поменяются какие-то данные
test_data = MainData()
url = 'https://yandex.ru/'


def test_create_file_on_yadisk(browser):
    login_page = LoginPage(browser, url)

    login_page.open()
    login_page.click_on_element(login_page.DZEN_LOGIN_BUTTON)
    login_page.login(test_data.user_data['login'], test_data.user_data['password'])
    # Залогинившись, переходим в Яндекс.Диск, дождавшись, пока форма авторизации исчезнет, иначе авторизация
    # может не засчитаться
    login_page.is_element_not_presented(login_page.AUTH_FORM)

    # Переходим на Яндекс.Диск
    browser.get('https://disk.yandex.ru/client/disk')
    yadisk_page = YandexDiskPage(browser, browser.current_url)
    yadisk_page.create_file(file_type=test_data.file_types['folder'], file_name=test_data.file_names[0])
    # Селектим папку
    yadisk_page.click_on_disk_item(item_name=test_data.file_names[0])

    yadisk_page.is_element_clickable(yadisk_page.SELECTED_ITEM)
    yadisk_page.press_enter(yadisk_page.SELECTED_ITEM)

    yadisk_page.create_file(file_type=test_data.file_types['text_doc'], file_name=test_data.file_names[1])

    yadisk_page.close_specific_window(window_index=1)  # Закрываем 2 вкладку с файлом
    yadisk_page.switch_to_another_window(window_index=0)  # Переключаемся на 1 вкладку и продолжаем работу

    # Ищем последний созданный файл в папке и сверяем его имя. Т.к. у файла появилось расширение .docx, конкатенируем
    # его исходное имя и расширение в одну строку
    yadisk_page.check_file_names(test_data.file_names[1] + test_data.file_extensions[1])


def test_upload_file_and_check_content(browser):
    login_page = LoginPage(browser, url)

    login_page.open()
    login_page.click_on_element(login_page.DZEN_LOGIN_BUTTON)
    login_page.login(test_data.user_data['login'], test_data.user_data['password'])
    login_page.is_element_not_presented(login_page.AUTH_FORM)

    browser.get('https://disk.yandex.ru/client/disk')
    yadisk_page = YandexDiskPage(browser, browser.current_url)
    yadisk_page.create_file(file_type=test_data.file_types['folder'], file_name=test_data.file_names[2])
    yadisk_page.click_on_disk_item(item_name=test_data.file_names[2])

    yadisk_page.is_element_clickable(yadisk_page.SELECTED_ITEM)
    yadisk_page.press_enter(yadisk_page.SELECTED_ITEM)

    # Убираем класс у инпута через скрипт JS, чтобы он стал видимым
    yadisk_page.make_upload_input_visible()

    yadisk_page.upload_file(yadisk_page.ULOAD_FILES_INPUT, test_data.local_files_data['txt_file_path'])
    yadisk_page.click_on_disk_item(test_data.file_names[3] + test_data.file_extensions[0])

    yadisk_page.is_element_clickable(yadisk_page.SELECTED_ITEM)
    yadisk_page.press_enter(yadisk_page.SELECTED_ITEM)

    yadisk_page.switch_to_another_window(window_index=1)  # Переключаемся на вкладку с содержимым файла

    # Считываем текст в открытом файле и проверяем его соответствие тексту в локальном файле
    yadisk_page.check_opened_file_text(yadisk_page.get_local_file_content(test_data.local_files_data['txt_file_path']))

    browser.switch_to.window(browser.window_handles[0])
    yadisk_page.click_on_element(yadisk_page.CANCEL_HIGHLIGHT_BUTTON)  # Закрыть окно выделения сверху, нажав на крестик
