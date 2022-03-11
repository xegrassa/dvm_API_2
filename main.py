import argparse
import os
from urllib.parse import urlparse

import requests
from dotenv import load_dotenv

BITLY_URL = 'https://api-ssl.bitly.com'


def shorten_link(token, url):
    """Возвращает Bitlink ссылку созданную для переданного url."""
    endpoint = f'{BITLY_URL}/v4/bitlinks'
    headers = {
        'Authorization': f'Bearer {token}'
    }
    payload = {
        'long_url': f'{url}'
    }
    response = requests.post(endpoint, headers=headers, json=payload)
    response.raise_for_status()
    bitlink = response.json()['link']
    parsed_link = urlparse(bitlink)

    return parsed_link.netloc + parsed_link.path


def count_clicks(token, bitlink):
    """Возвращает кол-во кликов по Bitlink ссылке."""
    endpoint = f'{BITLY_URL}/v4/bitlinks/{bitlink}/clicks/summary'
    headers = {
        'Authorization': f'Bearer {token}'
    }
    url_params = {
        'units': '-1',
    }
    response = requests.get(endpoint, headers=headers, params=url_params)
    response.raise_for_status()
    return response.json()['total_clicks']


def is_bitlink(token, url):
    """Проверяет что переданный url является Bitlink."""
    headers = {
        'Authorization': f'Bearer {token}'
    }
    endpoint = f'{BITLY_URL}/v4/bitlinks/{url}'
    response = requests.get(endpoint, headers=headers)
    return response.ok


def args_parse():
    parser = argparse.ArgumentParser(description='Укорачивает URL')
    parser.add_argument('url', type=str, help='URL который надо укоротить')
    return parser.parse_args()


def main(token, url):
    """Показывает Bitlink от URL или кол-во кликов по Bitlink.

    :param token: Токен полученный на сайте https://app.bitly.com/
    :param url: URL или Bitlink. ex: http://e1,ru | bit.ly/3CyjyTU
    """
    if not token:
        print('Отсутствует Token!')
        return

    if is_bitlink(token, url):
        try:
            total_clicks = count_clicks(token, url)
        except requests.exceptions.HTTPError:
            print(f'Неправильный Bitlink {url}')
            return
        else:
            print('Количество кликов', total_clicks)
    else:
        try:
            bitlink = shorten_link(token, url)
        except requests.exceptions.HTTPError:
            print(f'Неправильно введенный URL {url}')
            return
        else:
            print('Битлинк', bitlink)


if __name__ == '__main__':
    load_dotenv()
    token = os.getenv('token')
    args = args_parse()
    main(token, args.url)
