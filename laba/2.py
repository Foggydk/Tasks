from PIL import Image


original = Image.open("C:/Users/dkeyd/OneDrive/Desktop/Абобы/Обои/1x/Обои.png")

smaller = original.resize((int(original.width/3), int(original.height/3)))


mirror1 = original.transpose(Image.FLIP_LEFT_RIGHT)


mirror2 = original.transpose(Image.FLIP_TOP_BOTTOM)


smaller = smaller.convert('RGB')
smaller.save("smaller.jpg")

mirror1 = mirror1.convert('RGB')
mirror1.save("mirror1.jpg")

mirror2 = mirror2.convert('RGB')
mirror2.save("mirror2.jpg")


print("Изображения успешно сохранены.")
