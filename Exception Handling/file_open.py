f=None
try:
    f=open('else_block.py ',r)
except:
    print('some problems while locating/opening the file')
else:
    print('file opened successfully!!')
    print('The data present in the file is:')
    print('#'*30)
    print(f.read())
finally:
    if f is not None:
        f.close()
    