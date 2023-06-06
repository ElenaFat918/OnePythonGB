# Программа загадывает число от 0 до 1000.
# Необходимо угадать число за 10 попыток.
# Программа должна подсказывать “больше” или “меньше” после каждой попытки.
# Для генерации случайного числа используйте код:
#   from random import randint
# 	num = randint(LOWER_LIMIT, UPPER_LIMIT)


from random import randint


MIN = 0
MAX = 100
TRY = 2
RAND_NUM = randint(MIN, MAX)
winner = True
for _ in range(TRY + 1):
    number = int(input('Введи число от 0 до 1000: '))
    if number > RAND_NUM:
        print('Ваше число БОЛЬШЕ загаданного')
        winner = False
    elif number < RAND_NUM:
        print('Ваше число МЕНЬШЕ загаданного')
        winner = False
    else:
        print('УРАААА Вы выиграли!')
        winner = True
if not winner:
    print('Вы проиграли :(')