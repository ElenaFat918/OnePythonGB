# ✔ Напишите программу, которая получает целое число и
# возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.


num = int(input('Введите число в десятичной системе: '))
print(f'Встроенная функция hex -> \t\t{hex(num)}')

if not num:
    print('0x0')
result = ''
hex_letters = list('0123456789abcdef')
while num > 0:
    result = hex_letters[num % 16] + result
    num //= 16
print('Собственная функция self_hex -> 0x' + result)