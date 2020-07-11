import csv

with open('C:\Users\evgeniy.s\PycharmProjects\Otus_QA_Saganchi\hometask_files\data', 'r', encoding='utf-8') as f:
    reader = DictReader(f)

    # Итерируемся по данным делая из них словари
    for row in reader:
        print(row)
        print(row['first_name'])