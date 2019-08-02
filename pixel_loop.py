from PIL import Image
img = Image.open('smile.png')
for y in range(img.height):
  for x in range(img.width):
    pixel = img.getpixel((x, y))
    print(str(x) + ',' + str(y) + ': ' + str(pixel))
  print()
