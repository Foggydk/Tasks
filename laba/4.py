from PIL import Image


water_path = "C:/Users/dkeyd/OneDrive/Desktop/Абобы/Обои/1x/Обои.png"
base2 = "4.jpg"
output_image_path = "water_4.jpg"


with Image.open(water_path) as water:
    water.load()

base = Image.open(base2)
base = base.resize((water.size[0], water.size[1])).convert("L")

base1 = base.resize((100, 100))

with Image.open(base2) as background:
    background.load()

    background.paste(base1, (50, 50))

    background.save(output_image_path)
    background.show()

