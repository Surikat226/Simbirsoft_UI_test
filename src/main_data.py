import os


class MainData:
    # Данные заключены в списки/словари с уклоном на то, что, возможно, в будущем они будут пополняться

    user_data = {
        'login': 'lamapalooza333',
        'password': 'ilovejimmysmom'
    }

    file_names = [
        'Сурикаты',  # 0
        'Всё о сурикатах',  # 1
        'Йети',  # 2
        'Описание йети'  # 3
    ]

    file_types = {
        'folder': 'Папку',
        'text_doc': 'Текстовый документ'
    }

    file_extensions = [
        '.txt',  # 0
        '.docx'  # 1
    ]

    local_files_data = {
        'txt_file_path': os.path.abspath('src/test_files/Описание йети.txt')
    }
