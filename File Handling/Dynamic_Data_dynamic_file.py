fname=input('Enter file name:')
f=open(fname,'w')
while True:
    data=input('Enter data to write:')
    f.write(data+'\n')
    option=input('Do you want to add more data [yes|no]')
    if option.lower()=='no':
        break
print('your data is successully written to the file successfully!!!')
f.close()

