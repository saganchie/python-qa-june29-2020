import pytest
import random


@pytest.mark.parametrize('input_id, output_id',
                         [(10000, '10000'),
                             (-1, '-1'),
                             (0, '0')])
@pytest.mark.parametrize('input_title, output_title',
                         [('title', 'title'),
                             ('', ''),
                             (100, '100'),
                             ('&', '&')])
def test_api_post_request(api_client, input_id, output_id, input_title, output_title):
    res = api_client.post(
        path="/posts",
        data={'title': input_title, 'body': 'bar', 'userId': input_id})
    res_json = res.json()
    assert res_json['title'] == output_title
    assert res_json['body'] == 'bar'
    assert res_json['userId'] == output_id


# Параметр фильтрации постов по Id пользователя
# https://jsonplaceholder.typicode.com/posts?userId=1
@pytest.mark.parametrize('userId', [-1, 0, 'a', 11])
def test_api_empty_response(api_client, userId):
    res = api_client.get(
        path="/posts",
        params={'userId': userId}
    )
    # Проверяем что на таких данных ответ пустой
    assert res.json() == []


# Параметр фильтрации постов по Id пользователя
# https://jsonplaceholder.typicode.com/posts?userId=1
@pytest.mark.parametrize('userId, userId_in_response', [(1, 1), (2, 2), (10, 10)])
def test_api_filtering(api_client, userId, userId_in_response):
    response = api_client.get(
        path="/posts",
        params={'userId': userId}
    )
    # Проверка что случайный пост от пользователя с ожидаемым id
    response_json = response.json()
    random_post_number = random.randint(1, 9)
    assert len(response_json) > 0
    assert response.json()[random_post_number]['userId'] == userId_in_response
