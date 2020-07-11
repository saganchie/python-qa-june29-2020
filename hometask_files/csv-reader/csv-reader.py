import csv
from csv import DictReader

# with open('../data/data.csv', 'r') as file:
#    reader = csv.reader(file)
#    header = next(reader)
#    print(header)

#    for item in reader:
#        # print(item)
#        # print(dict(zip(header, item)))
#        print(dict(zip(header, item))['Title'])


with open('../data/data.csv') as k:
    reader = DictReader(k)

    # Итерируемся по данным делая из них словари
    for row in reader:
        print(row)
        # print(row['Title'])