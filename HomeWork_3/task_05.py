# Задание №5
# ✔ Создайте вручную список с повторяющимися целыми числами.
# ✔ Сформируйте список с порядковыми номерами нечётных элементов исходного списка.
# ✔ Нумерация начинается с единицы.


from random import randint

list_num = []
for i in range(0, 10):
    list_num.append(randint(0, 5))

print(list_num)
res = []
for i, elem in enumerate(list_num, start=1):
    if elem % 2:
        res.append(i)
        # print(f'{elem} % 2 = {elem % 2}')
print(res)

