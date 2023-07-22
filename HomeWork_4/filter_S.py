# Задание №8
# ✔ Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
# ✔ Напишите функцию, которая при запуске заменяет содержимое переменных оканчивающихся на s
# (кроме переменной из одной буквы s) на None.
# ✔ Значения не удаляются, а помещаются в одноимённые переменные без s на конце.


names = "Иван"
profile = "Николай"
juniors = "Пётр"
char_ = 's'


def replacement_with_s(*kwargs):
    kwargs = list(kwargs)
    temp = []
    global char_
    for i in range(len(kwargs)):
        if kwargs[i].endswith(char_) and kwargs[i] != char_:
            temp.append(kwargs[i])
            kwargs[i] = None
    for i in range(len(kwargs)):
        if kwargs[i] is not None:
            kwargs[i] += ''.join([i for i in temp])
    return kwargs


print(replacement_with_s(names="Иван", profile="Николай", juniors="Пётр" )

