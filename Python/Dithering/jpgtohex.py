from PIL import Image
import csv
from os.path import splitext
from glob import glob
import os
import sys

#img = Image.open("IMG_6464.jpg").convert('RGB')
def search():
    jpgList = glob('./*.jpg')

    print (jpgList)
    for jpg in jpgList:
        img = Image.open(jpg).convert('RGB')
        img.thumbnail((100,100))
        png = splitext(jpg)[0]+'.png'
        img.save(png,'PNG')

def rgb2hex(numTumple):
    r,g,b=list(numTumple)
    return '#{:02x}{:02x}{:02x}'.format(r,g,b)

def compress():
    img = Image.open('face.jpg').convert('RGB')
    img.thumbnail((100,100))
    img.save('face_100.jpg')

def arg():
    img = Image.open('face_100.jpg')
    file = open('example.csv','w')
    for y in range(img.height):
        for x in range(img.width):
            s = rgb2hex(img.getpixel( (x,y)) )
            if x != img.width-1:
                file.write(s+',')
            else:
                file.write(s+'\n')
    file.close()

def main():
    compress()
    arg()
    search()

if __name__ == '__main__':
    main()
