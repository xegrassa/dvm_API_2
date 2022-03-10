import argparse
import os
from urllib.parse import urlparse

import requests
from dotenv import load_dotenv


def shorten_link(token, url):
    URL = 'https://api-ssl.bitly.com/v4/bitlinks'
    headers = {
        'Authorization': f'Bearer {token}'
    }
    payload = {
        'long_url': f'{url}'
    }
    response = requests.post(URL, headers=headers, json=payload)

    link = response.json()['link']
    parsed_url = urlparse(link)
    return parsed_url.netloc + parsed_url.path


def args_parse():
    parser = argparse.ArgumentParser(description='Укорачивает URL')
    parser.add_argument('url', type=str, help='URL который надо укоротить')
    args = parser.parse_args()
    return args


def main(url):
    tokken = os.getenv('TOKKEN')
    print('Битлинк', shorten_link(tokken, url))


if __name__ == '__main__':
    load_dotenv()
    args = args_parse()
    main(args.url)
