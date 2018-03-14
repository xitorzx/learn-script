'''
Context Manager
'''
import os,sys

class File():
    def __init__(self,filename,mode):
        self.filename = filename
        self.mode = mode
    def __enter__(self):
        print ('Opening file' + self.filename)
        self.openfile = open(self.filename,self.mode)
        return self.openfile
    def __exit__(self, type, value, traceback):
        print ('Closing File' + self.filename)
        self.openfile.close()
