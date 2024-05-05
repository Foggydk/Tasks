otkritki = {
    "День рождения": "dr.jpg",
    "Новый год": "ng.jpg",
    "8 Марта": "8 mar.jpg",
    "День победы": "denpob.jpg"
}

prazdnik = input("К какому празднику вам нужна открытка? ")

if prazdnik in otkritki:
    print(f"Вы выбрали праздник '{prazdnik}'. Открытка к этому празднику: {otkritki[prazdnik]}")
else:
    print("Извините, у нас нет открытки к указанному празднику.")
