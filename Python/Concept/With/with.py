from CM import File
import os,sys
with File('context.txt','w') as f:
    print ('writing the file')
    f.write('Hi!')