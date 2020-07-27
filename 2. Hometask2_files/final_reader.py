import pytest
import itertools
from csv import DictReader

from json import loads
from json import dumps
import csv


def test_read_csv():
    # return dict_from_csv
    a = []
    with open("./data/data.csv", 'r') as books:  # менеджер контекста
        # import pdb; pdb.set_trace()
        reader = DictReader(books)
        for row in reader:
            a.append(row)
            # print(row)
        print(a)
    return reader

print(test_read_csv())


def test_read_json():
    # return dict_from_json
    with open('./data/data1.json', 'r') as file:
        j = file.read()
        peoples = loads(j)
    return peoples


print(test_read_json())


def create_example_object(json_object, csv_object):
    # return user
    pass


def create_final_list():
    dict_from_csv = test_read_csv()
    dict_from_json = test_read_json()
    final = []
    for book, user in list(itertools.zip_longest(dict_from_csv, dict_from_json)):
        final.append(create_example_object(book, user))
    pass

    return final


def json_write(final):
    pass


def main():
    final_list = create_final_list()
    json_write(final_list)
    pass
