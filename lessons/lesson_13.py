import requests
import random

r = requests.get('https://lms.ithillel.ua/')


def get_raw_quote(lang='ru'):
    url = 'https://api.forismatic.com/api/1.0/'
    params = {'method': 'getQuote',
              'format': 'json',
              'lang': 'ru',
              'key': random.randint(1, 999999)}
    responce = requests.get(url, params=params)
    return responce.json()


def get_quote(raw_quote):
    return raw_quote['quoteText']


def get_author(raw_quote):
    return raw_quote['quoteAuthor']


for requests_number in range(10):
    raw_quote = get_raw_quote()
    quote = get_quote(raw_quote)
    print(raw_quote)
# res = get_raw_quote()
# print(res)