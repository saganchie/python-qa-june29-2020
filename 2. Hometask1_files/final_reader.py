import json
import csv


def test_read_csv():
    # return_dict_from_csv
    with open("./data/data.csv", 'r') as books: # менеджер контекста
        cin = csv.DictReader(books)
        villi = [row for row in cin]
    return villi


def test_read_json():
    # return dict_from_json
    with open('./data/data1.json', 'r') as file: # менеджер контекста
        j = file.read()
        peoples = json.loads(j)
    return peoples


def create_example_object(book, people):
    return {
        "name": people["name"],
        "gender": people["gender"],
        "address": people["address"],
        "books": [
            {
                "title": book["Title"],
                "author": book["Author"],
                "height": book["Height"],
            }
        ],
    }


def test_create_final_list():
    dict_from_csv = test_read_csv()
    dict_from_json = test_read_json()
    final = []
    for book, user in zip(dict_from_csv, dict_from_json):
        final.append(create_example_object(book, user))
    return final



with open("./output.json", "w+") as output:
    output.write(
        json.dumps(test_create_final_list())
    )
