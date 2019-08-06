from PIL import Image
img = Image.open('flower.png')
value = img.getpixel((5, 5))
img.putpixel((5, 5), value + 100)
img.save('output.png')
