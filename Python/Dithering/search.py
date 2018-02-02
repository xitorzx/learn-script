import os
from glob import glob
from os.path import splitext

def search():
    jpgList = glob('*.jpg')    #get all file in current named in jpg
    name = []
    for jpg in jpgList:
        name.append( splitext(jpg)[0])
    return name
    
def showName(name):
    for n in name:
        print(n)
        
def main():
    name = search()
    showName(name)
    
if __name__=='__main__':
    main()
