# Задание №7
# Пользователь вводит строку текста.
# ✔ Подсчитайте сколько раз встречается каждая буква в строке без использования метода count и с ним.
# ✔ Результат сохраните в словаре, где ключ — символ, а значение — частота встречи символа в строке.
# ✔ Обратите внимание на порядок ключей. Объясните почему они совпадают или не совпадают в ваших решениях.


import regex
input_text = input('Введите строку текста: ')
print(input_text)
list_res = regex.findall(r'\X', input_text, regex.U)
print(list_res)
dict_res = {}
charCount = 0

for i in list_res:
    if i.isalpha():
        charCount += 1
        dict_res.setdefault(i, list_res.count(i))

print(charCount)
print(dict_res)


