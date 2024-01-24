import os
import random
import requests


def get_random_proxy():
    abs_path = os.path.dirname(__file__)
    file_path = os.path.join(abs_path, 'rotating_proxies_list.txt')
    proxies_list = open(file_path, "r").read().strip().split("\n")
    proxies = tuple(proxies_list)
    return random.choice(proxies)


def get(url, proxy):
    if not proxy:
        proxy = get_random_proxy()
    try:
        response = requests.get(url, proxies={'http': f"http://{proxy}"}, timeout=30)
        # print(response.status_code, proxy)
        return response.status_code, proxy
    except Exception as e:
        print(e)
        return None


def check_proxies():
    res, proxy = get("https://www.google.com/", None)
    valid_statuses = [200, 301, 302, 307, 404]
    if res not in valid_statuses:
        check_proxies()
    else:
        return proxy


if __name__ == '__main__':
    pass
