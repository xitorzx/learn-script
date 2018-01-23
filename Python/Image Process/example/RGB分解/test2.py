from PIL import Image
import sys
file = 1

img = Image.open('1.jpg').convert('RGB')
for y in range(img.height):
    for x in range(img.width):
        r,g,b = img.getpixel((x,y))
        img.merge=('RGB',(b,r,g))

img.save('2_output.jpg')
