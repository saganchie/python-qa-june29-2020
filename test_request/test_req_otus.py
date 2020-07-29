import requests
import pytest

host = 'http://httpbin.org/'


# @pytest.mark.parametrize(["h", "r_times", "exp_resp", "allow_red"], [(host, '3', '302', True)])
def test_redirect():
    url = 'http://httpbin.org/get'
    response = requests.get(url, allow_redirects=True)
    resp_json = response.json()
    assert response.status_code == 200

# http://httpbin.org/
# http://httpbin.org/redirect/{n}
# curl -X GET "http://httpbin.org/redirect/1" -H "accept: text/html"
#
#
# Написать простой тест на гет с параметром n - количество редиректов

# средиректило ли на него
# редирект ли это


