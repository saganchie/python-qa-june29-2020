import csv
from csv import DictReader
from json import loads
from json import dumps


# with open('../data/data.csv', 'r') as file:
#    reader = csv.reader(file)
#    header = next(reader)
#    print(header)

#    for item in reader:
#        # print(item)
#        # print(dict(zip(header, item)))
#        print(dict(zip(header, item))['Title'])

    # используем контекстный менеджер для чтения csv файла

with open('./data/data.csv', 'r') as data_from_csv:
    reader = DictReader(data_from_csv)

    # Итерируемся по данным делая из них словари

    for items in reader:
        print(items)
        # print(row['Title'])

    # используем контекстный менеджер для чтения json файла
with open('./data/data1.json', 'r') as file:
    j = file.read()
    n = loads(j)
    for people in n:
        print(people)
    # print(type(n))
    # print(type(dumps(n)))

    # Используем контекстный менеджер для записи json в фаил

with open('newest_json.json', 'w') as newfile:
    pass