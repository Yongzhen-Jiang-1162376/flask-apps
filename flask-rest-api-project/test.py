stores = [{'name': 'my first store', 'items': [{'name': 'coke', 'price': 2.02}]}]

a = 12

def get_store():
    return stores[0], a

def change_value():
    print(a)
    # a = 11

print(a)
