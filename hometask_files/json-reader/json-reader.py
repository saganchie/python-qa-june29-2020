from json import loads, dumps

with open('../data/data1.json', 'r') as file:
    j = file.read()
    n = loads(j)
    print(n)
    # print(type(n))
    # print(type(dumps(n)))
