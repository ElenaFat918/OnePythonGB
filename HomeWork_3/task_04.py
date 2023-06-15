# Задание №4
# ✔ Создайте вручную список с повторяющимися элементами.
# ✔ Удалите из него все элементы, которые встречаются дважды.


from random import randint

list_num = []
COUNT_NUM = 2

for i in range(0, 10):
    list_num.append(randint(0, 5))

print(list_num)
for item in list_num:
    if list_num.count(item) == COUNT_NUM:
        print(item)
        for i in range(COUNT_NUM):
            list_num.remove(item)
print(list_num)
