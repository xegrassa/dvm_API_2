import argparse
import os
from urllib.parse import urlparse

import requests
from dotenv import load_dotenv


class EmptyDataError(Exception):
    pass


BITLY_URL = 'https://api-ssl.bitly.com'


def shorten_link(token, long_url):
    """Возвращает Bitlink ссылку созданную для переданного url."""
    url = f'{BITLY_URL}/v4/bitlinks'
    headers = {
        'Authorization': f'Bearer {token}'
    }
    payload = {
        'long_url': f'{long_url}'
    }
    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()['link']


def count_clicks(token, bitlink):
    """Возвращает кол-во кликов по Bitlink ссылке."""
    headers = {
        'Authorization': f'Bearer {token}'
    }
    url_params = {
        'units': '-1',
    }

    parsed_link = urlparse(bitlink)
    link = parsed_link.netloc + parsed_link.path
    url = f'{BITLY_URL}/v4/bitlinks/{link}/clicks/summary'

    response = requests.get(url, headers=headers, params=url_params)
    response.raise_for_status()
    return response.json()['total_clicks']


def is_bitlink(token, url_to_check):
    """Проверяет что переданный url является Bitlink."""
    headers = {
        'Authorization': f'Bearer {token}'
    }

    parsed_url = urlparse(url_to_check)
    link = parsed_url.netloc + parsed_url.path
    url = f'{BITLY_URL}/v4/bitlinks/{link}'

    response = requests.get(url, headers=headers)
    return response.ok


def main():
    """Возвращает Bitlink или кол-во кликов по нему в зависимости от того что было передано в скрипт."""
    load_dotenv()
    token = os.getenv('BITLY_TOKEN')
    if not token:
        raise EmptyDataError('Отсутствует переменная окружения BITLY_TOKEN')

    parser = argparse.ArgumentParser(description='Укорачивает URL')
    parser.add_argument('url', type=str, help='URL который надо укоротить')
    args = parser.parse_args()

    try:
        if is_bitlink(token, args.url):
            total_clicks = count_clicks(token, args.url)
            print('Количество кликов', total_clicks)
        else:
            bitlink = shorten_link(token, args.url)
            print('Битлинк', bitlink)
    except requests.exceptions.HTTPError:
        print(f'Некоректно введенный URL/Bitlink: {args.url}')


if __name__ == '__main__':
    main()
