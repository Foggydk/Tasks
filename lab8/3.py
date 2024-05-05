from PIL import Image, ImageDraw, ImageFont
otkritki = {
    "День рождения": "dr.jpg",
    "Новый год": "ng.jpg",
    "8 Марта": "8 mar.jpg",
    "День победы": "denpob.jpg"
}

prazdnik = input("К какому празднику вам нужна открытка? ")
name = input("Введите имя того, кторое нужно вписать в открытку: ")

if prazdnik in otkritki:
    otkritka = otkritki[prazdnik]

    image = Image.open(otkritka)

    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype("ofont.ru_Bubblez-Graffiti.ttf", 20)

    color = (0, 0, 225)

    text_width, text_height = draw.textlength(f"{name}, поздравляю", font=font)

    x = (image.width - text_width) // 2
    y = (image.height - text_height) // 2

    draw.text((x, y), f"{name}, поздравляю", font=font, fill=color)

    image.save(f"new_{otkritka}", "png")

    print(f"Открытка для {name} сохранена в файл new_{otkritka}.")
else:
    print("Извините, у нас нет открытки к указанному празднику.")
