import os
from urllib.parse import urlparse

import requests
from dotenv import load_dotenv

# URL = 'https://api-ssl.bitly.com/v4/user'
URL = 'https://api-ssl.bitly.com/v4/bitlinks'


def shorten_link(token, url):
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


def main():
    tokken = os.getenv('TOKKEN')
    print('Битлинк', shorten_link(tokken, URL))


if __name__ == '__main__':
    load_dotenv()
    main()
