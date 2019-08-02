from PIL import Image

img = Image.open('dragonfly.png') 
print('Width: ' + str(img.width)) 
print('Height: ' + str(img.height))
