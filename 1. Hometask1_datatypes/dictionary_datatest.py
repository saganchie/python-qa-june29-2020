import pytest


# Создаем словарь при помощи dict(), получаем значение по ключу, проверяем что получили нужное значение

def test_dict_one():
    first_second_name = [['Patrick', 'Bonkowski'], ['Evgeniy', 'Elchugin'], ['Ksenia', 'Shkola'],
                         ['Anastasia', 'Grishina']]
    name_dict = dict(first_second_name)
    print(name_dict)
    name_dict['Sergey'] = 'Samborskiy'
    print(name_dict)
    assert 'Sergey' in name_dict

# dict1 = {'Elcugin': 1, 'Patrick': 2}
# dict2 = {'Ksuha': 3, 'Sinegovskaya': 4}
