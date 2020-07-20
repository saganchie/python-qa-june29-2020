import pytest

# Создаем множество из списка при помощи set.
# Проверяем, что во множество был добавлен элемент
# и он есть в этом множестве

def test_set_one():
    numbers = [1, 2, 3, 2, 3, 4, 5]
    set_numbers = set(numbers)
# print(set_numbers)
    set_numbers.add('666')
# print(set_numbers)
    assert '666' in set_numbers


"""

Создаем множество из списка при помощи set.
Проверяем, что из множества был удален элемент
и его нет в этом множестве

"""

def test_set_two():
    days = ['Monday','Tuesday', 'Saturday', 'Friday','Monday']
    set_days = set(days)
    #print(set_days)
    set_days.remove('Friday')
    #print(set_days)
    assert 'Friday' not in set_days

# Объединение множеств

def test_set_three():
    set_one = {'Patrick', 'Ksuha'}
    set_two = {'Serega', 'Jeka'}


def test_set_four():
    



