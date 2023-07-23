# Урок 11. ООП. Особенности Python
# Решить задания, которые не успели решить на семинаре.
# Добавьте ко всем задачам с семинара строки документации и методы вывода информации на печать.
# Создайте класс Матрица. Добавьте методы для: - вывода на печать,
# сравнения, сложения, умножения матриц


class Matrix:

    def __init__(self, lists: list[list[int]]):  # cписок списков, представляющий матрицу.
        self.lists = lists

    def __str__(self):  # строковое представление матрицы
        result = ''
        for row in self.lists:
            for item in row:
                result += ''.join(f'{item}\t')
            result += ''.join('\n')
        return result

    def __eq__(self, other):  # сравнениe матриц на равенство
        return True if self.lists == other.lists else False

    def __add__(self, other):  # сложениe матриц
        result = []
        row = []
        for i in range(len(self.lists)):
            for j in range(len(self.lists[0])):
                row.append(self.lists[i][j] + other.lists[i][j])
            result.append(row)
            row = []
        return Matrix(result)

    def __mul__(self, other):  # умножениe матриц.
        m = len(self.lists)
        n = len(other.lists)
        k = len(other.lists[0])
        result = [[0 for _ in range(k)] for _ in range(m)]
        for i in range(m):
            for j in range(k):
                result[i][j] = sum(self.lists[i][k] * other.lists[k][j] for k in range(n))
        return Matrix(result)


if __name__ == '__main__':
    matrix_1 = Matrix([[3, 3, 3], [3, 3, 3], [3, 3, 3]])
    matrix_2 = Matrix([[3, 3, 3], [3, 3, 3], [3, 3, 3]])

    matrix_sum = matrix_1 + matrix_2
    print(matrix_sum)

    matrix_mul = matrix_1 * matrix_2
    print(matrix_mul)

    if matrix_1 == matrix_2:
        print('Матрицы равны')
    else:
        print('Матрицы не равны')
