#from PIL import Image

from cmath import pi as PI

#img = Image.open('IMG_6464.jpg').convert('L')

def sigma(func,frm,to):
    result=0
    for i in range(frm, to+1):
        result=result+func(i)
    return result


#img.save('new.png')

