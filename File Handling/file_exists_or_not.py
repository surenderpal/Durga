import os
fname=input('Enter file name:')
if os.path.isfile(fname):
    print('File exists:',fname)
    with open(fname,'r') as f:
        text=f.read()
        print('The content of the file is:')
        print('*'*40)
        print(text,end='')
        print('*'*40)
else:
    print("File doesn't exitst:",fname)
