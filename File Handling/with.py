with open('with.txt','w') as f:
    f.write('surender\n')
    f.write('will\n')
    f.write('become\n')
    f.write('Data Scientist\n')
    print('Is file closed:',f.closed)
print('Is file closed outside with block:',f.closed)
