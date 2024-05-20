import json
with open('products.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

new_product = {
    "name": input("Введите название товара: "),
    "price": input("Введите стоимость товара: "),
    "available": input("Товар в наличие? "),
    "weight": int(input("Введите вес товара: "))
}
data["products"].append(new_product)
with open('spis.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, indent=4)
with open('spis.json', 'r', encoding='utf-8') as file:
    new_data = json.load(file)

for products in new_data['products']:
    print(f'Название: {products["name"]}'
          '\n' f' Цена: {products["price"]}'
          '\n' f' Вес: {products["weight"]}')
    if products['available']:
        print("В Наличии")
    else:
        print('Нет в наличии')