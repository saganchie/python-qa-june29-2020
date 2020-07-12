import pytest

# тесты с типом данных string

def test_string_one():
    second_name = 'Evgeniy'
    assert second_name[0] == 'E'


def test_string_two():
    long_name = 'evgeniysaganchy'
    assert long_name[7:] == 'saganchy'


def test_string_three():
    big_name = 'evgeniysaganchi' + 'igorevich'
    assert big_name != 'evgeniysaganciigorevich'

def test_string_four():

def test_string_five():
