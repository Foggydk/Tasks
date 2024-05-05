from PIL  import Image

def imageobr(input_image, output_image, left, top, right, bottom):
    image = Image.open(input_image)
    image1 = image.crop((left, top, right, bottom))
    image1.save(output_image)


image2 = "7ae9a03e9eadb755ff7d4cd340e40fee.jpg"

left = 180
top = 70
right = 385
bottom = 363


image3 = "обрезанная_открытка.jpg"


imageobr(image2, image3, left, top, right, bottom)

print("Изображение успешно обрезано и сохранено")
