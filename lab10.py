import os
import json
def num1_2():
    with open("lab10.json", mode="r", encoding='utf8') as file:
        rfile = json.load(file)
        secondfile = (rfile['products'])
        for i in range(3):
            print("Название", secondfile[i]['name'])
            print("Цена", secondfile[i]['price'])
            print("Вес", secondfile[i]['weight'])
            if secondfile[i]['available'] == True:
                print("В наличии")
            else:
                print("Нет в наличии!")
    new_product = {}
    new_product['name'] = input("Введите название продукта: ")
    new_product['price'] = int(input("Введите цену продукта: "))
    new_product['available'] = input("Есть ли продукт в наличии (True/False): ")
    new_product['weight'] = int(input("Введите вес продукта: "))

    rfile['products'].append(new_product)

    with open('lab10.json', 'w') as file:
        json.dump(rfile, file, indent=2)

    for product in rfile['products']:
        availability = "В наличии" if product['available'] else "Нет в наличии!"
        print(f"Название: {product['name']}")
        print(f"Цена: {product['price']}")
        print(f"Вес: {product['weight']}")
        print(availability)
        print()
    num1_2()


def num3():
    dic = {}
    with open("словарь.txt", mode="r", encoding='utf8') as file:
        lines = file.read().splitlines()

    for line in lines:
        word = line.strip().split(' - ')
        if len(word) == 2:
            en = word[0]
            ru = word[1].split(", ")
            for w in ru:
                dic[w] = en
    sort = dict(sorted(dic.items()))
    with open("словарь2.txt", 'w', encoding='utf-8') as f:
        for ru_word, en_word in sort.items():
            f.write(f'{ru_word} - {en_word}\n')
    print(dic)
num3()