from PIL import Image

file_path = "C:/Users/dkeyd/OneDrive/Desktop/Абобы/Обои/1x/Обои.png"

img = Image.open(file_path)

print("Размер изображения:", img.size)
print("Формат:", img.format)
print("Цветовая модель:", img.mode)

img.show()
