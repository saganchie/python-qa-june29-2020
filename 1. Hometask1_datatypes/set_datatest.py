import pytest

# Создаем множество при помощи set. Проверяем, что во множество был добавлен элемент
# и он есть в этом множестве

numbers = [1, 2, 3, 2, 3, 4, 5]
def test_set_one():
    set_numbers = set(numbers)
# print(set_numbers)
    set_numbers.add('666')
# print(set_numbers)
    assert '666' in set_numbers



# Проверка на то


# Проверка на то


# Проверка на то


# Проверка на то