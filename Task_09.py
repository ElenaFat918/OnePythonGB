# Задание №9.
# 📌 Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.


MIN = 2
MAX = 9
END = 10
for i in range(MIN, MAX + 1):
    for j in range(MIN, END + 1):
        print(f'{i} x {j} = {i * j}')
    print(' ')