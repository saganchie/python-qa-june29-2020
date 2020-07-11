import csv
from csv import DictReader

encoding='utf-8'

with open('../hometask_files/data', 'r') as f:
    reader = DictReader(f)

    # Итерируемся по данным делая из них словари
    for row in reader:
        print(row)
        print(row['first_name'])