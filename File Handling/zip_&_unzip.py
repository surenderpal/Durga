# #how to perform zip operations
# from zipfile import *
# f=ZipFile('files09042020.zip','w',ZIP_DEFLATED)
# f.write('binary.py')
# f.write('close.py')
# f.write('Dynamic.py')
# print('files09042020.zip created successfully')
 
#how to perform unzip operatios
from zipfile import *
f=ZipFile('files09042020.zip','r',ZIP_STORED)
names=f.namelist()
print('File names are:',names)
for name in names:
    with open(name,'r') as f1:
        data=f1.read()
        print('*'*80)
        print('file name:',name)
        print('content of the file:')
        print(data,end='')
        print('*'*80)
