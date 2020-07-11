import csv
from csv import DictReader



with open('..data/data.csv', 'r', encoding='utf-8') as f:
    reader = DictReader(f)

    # Итерируемся по данным делая из них словари
    for row in reader:
        print(row)
        print(row['first_name'])