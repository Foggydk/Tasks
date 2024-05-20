import json
with open('products.json') as f:
    data = json.load(f)
products = data['products']
for product in products:
    print("Название:", product['name'])
    print("Цена:", product['price'])
    print("Вес:", product['weight'])
    if product['available']:
        print("В наличии")
    else:
        print("Нет в наличии!")
    print()
