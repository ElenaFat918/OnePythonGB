import csv


def create_csv_file():
    fieldnames = ['Предметы:']
    items = ['Русский язык', 'Литература', 'Математика', 'Физика', 'История']

    with open('school_lessons.csv', mode='w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for item in items:
            writer.writerow({'Предметы:': item})


create_csv_file()
