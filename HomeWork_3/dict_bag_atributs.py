# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант. *Верните все возможные варианты комплектации рюкзака.


import random


list_atribute = {"бутерброды": 550, "пирог": 1000, "зонт": 1500, "телефон": 300, "плед": 3000, "спрей": 200, "салат": 500}
print(' Сформирван словарь: ', list_atribute)

MAX = 5000
COUNT = 0
dict_atribute = []

while COUNT < MAX:
    key, value = random.choice(list(list_atribute.items()))
    if key in dict_atribute:
        continue
    if COUNT + value > MAX:
        break
    COUNT += value
    dict_atribute += (str(key), str(value))

print(dict_atribute, "=", COUNT)
