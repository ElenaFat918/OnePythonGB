# На семинаре 13 был создан проект по работе с пользователями (имя, id, уровень).
# Напишите 3-7 тестов pytest для данного проекта.
# Используйте фикстуры.


import pytest
from Students import Student


@pytest.fixture
def setup_names():
    return [["Марина", "Иванова"], ["Роман", "Бубликов"]]


def test_name(setup_names):
    list_names = setup_names
    for name in list_names:
        student = Student(name[0], name[1])
        if student._name != name[0] or student._surname != name[1]:
            print("test faild")


@pytest.fixture
def setup_grades():
    return [["Русский языкк", (5, 4, 4)], ["Литература", (5, 5, 5)], ['Математика', (5, 5, 5)]]


def test_grades(setup_grades):
    # list_grades = setup_grades
    for grades in setup_grades:
        student = Student("Анастасия", "Кондакова")
        student.grades.update({grades[0]: grades[1]})
        if grades[0] not in student.grades.keys() or (
                grades[0] in student.grades.keys() and student.grades[grades[0]] != grades[1]):
            print("test faild")


@pytest.fixture
def setup_tests():
    return [["Физика", (80, 73, 95)], ["История", (70, 85, 90)]]


def test_tests(setup_tests):
    list_tests = setup_tests
    for tests in list_tests:
        student = Student("Анастасия", "Кондакова")
        student.grades.update({tests[0]: tests[1]})
        if tests[0] not in student.grades.keys() or (
                tests[0] in student.grades.keys() and student.grades[tests[0]] != tests[1]):
            print("test faild")