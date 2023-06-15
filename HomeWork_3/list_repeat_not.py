# Дан список повторяющихся элементов.
#     Вернуть список с дублирующимися элементами.
#     В результирующем списке не должно быть дубликатов.


# Дан список повторяющихся элементов.
# * Вернуть список с дублирующимися элементами.
# * В результирующем списке не должно быть дубликатов.

from random import randint

list_num = []

for i in range(0, 10):
    list_num.append(randint(0, 5))
print(list_num)

COUNT = 0
set_result = []

for i in list_num:
    for j in list_num:
        if i == j:
            COUNT += 1
            if j not in set_result and COUNT > 1:
                set_result.append(j)
    COUNT = 0
print(f"Список дублирующихся элементов без дубликатов {set_result}")