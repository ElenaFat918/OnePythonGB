# Напишите функцию принимающую на вход только ключевые
# параметры и возвращающую словарь, где ключ — значение
# переданного аргумента, а значение — имя аргумента. Если
# ключ не хешируем, используйте его строковое представление.


def func(first_arg: int, second_arg: str) -> dict[str, int]:
    result = {}
    l = 0
    for f, s in zip(first_arg, second_arg):
        result[f] = second_arg[l]
        l += 1
    return result


second_arg = ['Victor', "Anna", 'Svetlana']
first_arg = [25, 27, 29]

print(func(first_arg, second_arg))
