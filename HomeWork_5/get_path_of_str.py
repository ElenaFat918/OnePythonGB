# Напишите функцию, которая принимает на вход строку —
# абсолютный путь до файла. Функция возвращает кортеж из трёх
# элементов: путь, имя файла, расширение файла.


file_path = "C:/gitEduc/python/картинка.jpg"

def get_path_of_str(file_path)->[]:
    file_path_components = file_path.split('/')
    file_name_and_extension = file_path_components[-1].rsplit('.', 1)
    return file_path, file_name_and_extension[0], file_name_and_extension[1]
print(get_path_of_str(file_path))