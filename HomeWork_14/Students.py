import csv
from statistics import mean


class NameVerification:
    def __set_name__(self, owner, name):
        self.private_name = '_' + name

    def __get__(self, obj, objtype=None):
        return getattr(obj, self.private_name)

    def __set__(self, obj, value):
        self._verification_name(value)
        setattr(obj, self.private_name, value)

    def _verification_name(self, value):
        if not isinstance(value, str):
            raise AttributeError('Имя должно быть строкой')
        if not value.isalpha():
            raise AttributeError('Имя должно состоять из букв')
        if not value.istitle():
            raise AttributeError('Имя должно начинаться с заглавной буквы')


class ItemValidator:

    def __init__(self, min_value: int = None, max_value: int = None):
        self._min_value = min_value
        self._max_value = max_value

    def __set_name__(self, owner, name):
        self.private_item = '_' + name

    def __get__(self, obj, objtype=None):
        return getattr(obj, self.private_item)

    def __set__(self, obj, value: dict):
        self._verification_range(value)
        self._verification_lessons(value)

        setattr(obj, self.private_item, value)

    def _verification_range(self, value: dict):
        for value in value.values():
            for value_tuple in value:
                if not isinstance(value_tuple, int):
                    raise TypeError(f'Значение {value_tuple} должно быть целым числом')
                if value_tuple is not None and value_tuple < self._min_value:
                    raise ValueError(f'Значение {value_tuple} должно быть больше или равно {self._min_value}')
                if value_tuple is not None and value_tuple > self._max_value:
                    raise ValueError(f'Значение {value_tuple} должно быть меньше или равно {self._max_value}')

    def _verification_lessons(self, value: dict):
        data = self._load_data()
        valid = 0
        for d in data:
            for v in value:
                if d == v:
                    valid += 1
        if valid != len(value):
            raise AttributeError(f'Предмета нет в списке')

    def _load_data(self):
        data = {}
        file_name = 'school_lessons.csv'
        i = 0
        with open(file_name, encoding='utf-8') as f:
            csv_reader = csv.reader(f)
            for item in csv_reader:
                res = ''.join(item).strip()
                i += 1
                if i != 1:
                    data[res] = None
        return data


class Student:
    _name: str = NameVerification()
    _surname: str = NameVerification()
    grades: dict = ItemValidator(2, 5)
    tests: dict = ItemValidator(0, 100)

    def __init__(self):
        self._name: str = ''
        self._surname: str = ''
        self._grades: dict[str: tuple] = {}
        self._tests: dict[str: tuple] = {}

    def __init__(self, first_name="", last_name=""):
        self._name = first_name
        self._surname = last_name
        self._grades: dict[str: tuple] = {}
        self._tests: dict[str: tuple] = {}

    def __str__(self):
        grades = '\n'.join(f'{k}: {v}' for k, v in self._grades.items())
        tests = '\n'.join(f'{k}: {v}' for k, v in self._tests.items())
        avg_test_results = '\n'.join(f'{k}: {v}' for k, v in self._avg_tests().items())
        avg_grades_result = '\n'.join(f'{k}: {v}' for k, v in self._avg_grades().items())
        return f'Студент:\n{self._name} {self._surname}' \
               f'\n\nОценки по предметам:\n{grades}' \
               f'\n\nОценки по тестам:\n{tests}' \
               f'\n\nСредняя оценка по тестам:\n{avg_test_results}' \
               f'\n\nСредняя оценка по всем предметам:\n{avg_grades_result}'

    def _avg_tests(self):
        avg_results = dict()
        for key, value in self._tests.items():
            avg_results[key] = round(mean(value), 1)
        return avg_results

    def _avg_grades(self):
        avg_result = 0
        for values in self._grades.values():
            avg_result += mean(values)
        return {'Средний балл по всем предметам': round(avg_result / len(self._grades.values()), 1)}


if __name__ == '__main__':
    student = Student()
    student._name = 'Марина'
    student._surname = 'Иванова'

    student.grades = {'Русский язык': (5, 4, 4), 'Литература': (4, 3, 5), 'Математика': (5, 5, 5)}
    student.tests = {'Физика': (80, 73, 95), 'История': (70, 85, 90)}
    print(student)