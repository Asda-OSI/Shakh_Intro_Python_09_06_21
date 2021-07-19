persons = {'John': 12, 'Jack': 34}

persons_other = {'Anna': 42, 'Jack': 64}

persons_result = {}

# persons_result.update(persons)
# persons_result.update(persons_other)

persons_result = {**persons, **persons_other}

print(persons_result)
print(max(list(persons.values()) + list(persons_other.values())))

products = [{'name': 'water', 'price': 12, 'title': 'Bonaqua'},
            {'name': 'bread', 'price': 7, 'title': 'Baton'},
            {'name': 'bread', 'price': 9, 'title': 'WhiteBread'},
            {'name': 'apple', 'price': 25, 'title': 'Golden'}]

bread_prices = []
for product in products:
    if product['name'] == 'bread':
    # product['sale'] = True
    #     bread_prices.append(product['price'])
        product['price'] = product['price'] * 1.1 - 1
print(products)