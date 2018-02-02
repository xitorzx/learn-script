from PIL import Image


def rgb2hex(numTumple):
    r,g,b=list(numTumple)
    return '#{:02x}{:02x}{:02x}'.format(r,g,b) #for hex code format output

def compress():
    img = Image.open('IMG_6464.jpg').convert('RGB')
    img.thumbnail((300,300))
    img.save('IMG_6464_300.jpg')

def main():
    compress()
if __name__ == '__main__':
    main()
