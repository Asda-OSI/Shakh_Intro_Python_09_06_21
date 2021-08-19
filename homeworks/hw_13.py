import requests
import random
import csv


# 1
def get_unique_quote(number):
    unique_quotes = []
    quote_dict = {}
    while len(unique_quotes) != number:
        url = "http://api.forismatic.com/api/1.0/"
        params = {"method": "getQuote",
                  "format": "json",
                  "key": random.randint(1, 999999)
                  }
        response = requests.get(url, params=params)
        raw_quote = response.json()
        print(raw_quote)
        if len(raw_quote['quoteAuthor']) != 0:
            quote_dict['Author'] = raw_quote['quoteAuthor']
            quote_dict['Quote'] = raw_quote['quoteText']
            quote_dict['URL'] = raw_quote['quoteLink']
            unique_quotes.append(quote_dict)
        quote_dict = {}
    print(unique_quotes)
    return unique_quotes


# 2
def write_to_csv(number, filename='unique_quotes.csv'):
    data = get_unique_quote(number)
    fieldnames = data[0].keys()
    with open(filename, "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


write_to_csv(5)
