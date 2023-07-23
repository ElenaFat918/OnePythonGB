# Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК.
# Соберите информацию о содержимом в виде объектов namedtuple.
# Каждый объект хранит:
# * имя файла без расширения или название каталога,
# * расширение, если это файл,
# * флаг каталога,
# * название родительского каталога.
# В процессе сбора сохраните данные в текстовый файл используя логирование.

import os
import logging
from collections import namedtuple

# Создаем namedtuple для хранения информации о файле/каталоге
FileInfo = namedtuple('FileInfo', "name extension is_dir parent")

# Конфигурируем логирование
logging.basicConfig(filename='info.log', level=logging.INFO, format='%(message)s')


def collect_directory_info(dir_path):
    # Проверяем, существует ли указанная директория
    if not os.path.exists(dir_path):
        raise ValueError(f'Directory does not exist: {dir_path}')

    # Получаем список файлов и каталогов в указанной директории
    for path, *_ in os.walk(dir_path):
        for item in os.listdir(path):
            lsp = item.strip(".").split(".")  # избавляемся от "." и делим по точке в середине
            name = lsp[0]  # имя файла без расширения или название каталога
            flag_dir = os.path.isdir(os.path.join(path, item))  # собрали путь и проверили его на директорию
            if len(lsp) == 2:
                extension = lsp[1]  # расширение
            else:
                extension = None
            parent = os.path.basename(path)  # отсекаем весь путь от папки (родительский каталог)

            # Создаем объект FileInfo и записываем информацию в лог-файл
            file_info = FileInfo(name, extension, flag_dir, parent)
            logging.info(file_info)


if __name__ == '__main__':
    directory_path = r'C:\Users\Райан\PycharmProjects\OnePythonGB'

    try:
        collect_directory_info(directory_path)
    except ValueError as e:
        print(e)