from PIL import Image, ImageDraw, ImageFont

image = Image.open(r'8 mar.jpg')
    draw = ImageDraw.Draw(party)
    x = input("введите имя которое нужно вписать: ")
    text = str(x) + ', поздравляю! '
    font = r"ofont.ru_Bubblez-Graffiti.ttf"
    font = ImageFont.truetype(font_path, size=20)
    y = draw.textlength(text, font=font)
    z = image.size
    w = (z[0] // 2) - (y // 2)
    image.text((w, 10), text, font=font, fill=("#EEE8AA"))
    image.save(r'C:\Users\Danil\Pycharm\lab8')
    image.show()
