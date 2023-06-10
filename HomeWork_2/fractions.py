# ✔ Напишите программу, которая принимает две строки вида
#   “a/b” — дробь с числителем и знаменателем.
# Программа должна возвращать сумму и * произведение дробей.
# Для проверки своего кода используйте модуль fractions.


import fractions


num1: int = int(input("Введите числитель первой дроби "))
num2: int = int(input("Введите знаменатель первой дроби "))
num3: int = int(input("Введите числитель второй дроби "))
num4: int = int(input("Введите знаменатель второй дроби "))

print((num1 / num2) + (num3 / num4))
print((num1 / num2) * (num3 / num4))
fraction1 = fractions.Fraction(num1, num2)
fraction2 = fractions.Fraction(num3, num4)
print(fraction1 + fraction2)
print(fraction1 * fraction2)
