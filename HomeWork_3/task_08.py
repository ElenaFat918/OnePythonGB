# Задание №8
# ✔ Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей.
# Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции с множествами.
# Код должен расширяться на любое большее количество друзей.

dict_bags = {"Лариса": ("бутерброды", "пирог", "зонт", "телефон"),\
                        "Михаил": ("вода", "плед", "спрей", "телефон"),\
                        "Соня": ("салат", "однораз_посуда", "сок")}
print(' Сформирван словарь: ', dict_bags)


list_atribute = []
for atribut in dict_bags.values():
    list_atribute += atribut
print('Какие вещи взяли все три друга? Вот эти: ', list_atribute)

print("вещи уникальны, есть только у одного друга: ")
count = 0
for i in list_atribute:
    for j in list_atribute:
        if j == i:
            count += 1
            print(j)

unicum_atribute = []
new_dict = {}
count = 0
for key, value in dict_bags.items():
    unicum_atribute.append(key)
    new_dict[key] = []
    for j in value:
        for k in list_atribute:
            if k == j:
                count += 1
        if count == 1:
            new_dict[key] += [j]
        if count > 1:
            unicum_atribute.remove(key)
        count = 0
print("у этого списка людей отсутствует вещь, которая дублируется у остальных", unicum_atribute)
