# Напишите функцию, которая получает на вход директорию
# и рекурсивно обходит её и все вложенные директории.
# Результаты обхода сохраните в файлы json, csv и pickle.


import json


def rec_json(file_name: str) -> None:
    di = {}
    with open(file_name, 'r', encoding='utf-8') as f:
        for line in f:
            li = line.split('/')

            di[str(li[0].capitalize())] = str(li[1])
        print(di)

    with open('new_json.json', 'w', encoding='utf-8') as f:
        json.dump(di, f, ensure_ascii=False, indent=2)


rec_json('directory.txt')
