import csv
from csv import DictReader
from json import loads, dumps

# with open('../data/data.csv', 'r') as file:
#    reader = csv.reader(file)
#    header = next(reader)
#    print(header)

#    for item in reader:
#        # print(item)
#        # print(dict(zip(header, item)))
#        print(dict(zip(header, item))['Title'])


with open('../hometask_files/data/data.csv', 'r') as k:
    reader = DictReader(k)

    # Итерируемся по данным делая из них словари
    for row in reader:
        print(row)
        # print(row['Title'])


with open('../hometask_files/data/data1.json', 'r') as file:
    j = file.read()
    n = loads(j)
    print(n)
    # print(type(n))
    # print(type(dumps(n)))
