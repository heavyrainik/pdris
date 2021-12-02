import requests


def test_post_spread_api():
    r = requests.get("http://python_app:5000/")
    print(r.status_code)


if __name__ == '__main__':
    test_post_spread_api()

