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

# Объединяем множества, проверяем, что подмножество входит во множество

def test_set_three():
    set_one = {'Patrick', 'Ksuha'}
    set_two = {'Serega', 'Jeka'}
    all_set = set_one.union(set_two)
    #print(all_set)
    assert set_one.issubset(all_set)


def test_set_four():
    first_set = {'Patrick', 'Ksuha', 'Serega', 'Elchugin'}
    second_set = {'Elchugin', 'Rita', 'Grishina'}

    pass


set1 = {1, 2, 3, 4}
set2 = {3, 6, 5}

@pytest.mark.parametrize('news_set_test', set1, set2)
def test_set_six(news_set_test):
    last_set = set1.intersection(set2)
    assert last_set == 3






# set1 = {'Patrick', 'Ksuha', 'Serega', 'Elchugin'}
# set2 = {'Elchugin', 'Rita', 'Grishina'}
#
# def inter():
#     new = set1.intersection(set2)
#     print(new)
#
# inter()