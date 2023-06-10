# Программа загадывает число от 0 до 1000.
# Необходимо угадать число за 10 попыток.
# Программа должна подсказывать “больше” или “меньше” после каждой попытки.
# Для генерации случайного числа используйте код:
#       from random import randint
# 	    num = randint(LOWER_LIMIT, UPPER_LIMIT)


from random import randint


MIN = 0
MAX = 1000
TRY = 10
RAND_NUM = randint(MIN, MAX)

while TRY > 0:
    number = int(input('Введи число от 0 до 1000: '))
    if number > RAND_NUM:
        print(f'Ваше число БОЛЬШЕ загаданного, осталось {TRY-1} попыток')
        TRY -= 1
    elif number < RAND_NUM:
        print(f'Ваше число МЕНЬШЕ загаданного, осталось {TRY-1} попыток')
        TRY -= 1
    else:
        print('УРАААА Вы выиграли!')
        break
else:
    print('Вы проиграли :(')
