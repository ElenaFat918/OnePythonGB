# Урок 13. Исключения
# Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях.
# Напишите к ним классы исключения с выводом подробной информации.
# Поднимайте исключения внутри основного кода. Например нельзя создавать
# прямоугольник со сторонами отрицательной длины.


from math import pi


class InvalidRadiusTypeError(Exception):
    def __init__(self, msg="Радиус должен быть > 0! "):
        self.msg = msg
        super().__init__(self.msg)


def area_round(r):
    if type(r) != int or type(r) != float:
        raise InvalidRadiusTypeError("Введите цифры")
    if r <= 0:
        raise InvalidRadiusTypeError()
    return round(pi * r ** 2, 2)


print(area_round("hb"))
