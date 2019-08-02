from PIL import Image
img = Image.open('smile.png')
pixel_value = img.getpixel((4, 0))
print(pixel_value)
