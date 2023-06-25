# Напишите функцию для транспонирования матрицы


A = [[7, 8, 9], [4, 5, 6]]


def transpose_matrix(A: list):
    print([*zip(*A)])


transpose_matrix(A)
