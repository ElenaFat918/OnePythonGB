# Задание №6
# Пользователь вводит строку текста. Вывести каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так,
# чтобы у самого длинного слова был один пробел между ним и номером строки.


input_str = input("Введите строку текста: ")
list_words = input_str.split()
max_len = len(list_words[0])
for i in list_words:
    if len(i) > max_len:
        max_len = len(i)

list_words.sort()
for num_line, line in enumerate(list_words, start=1):
    print(f"{num_line} {line:>{max_len}}")
