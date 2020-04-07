fname=input('enter file name:')
f=open('fname','w')
while True:
    data=input('Enter data to write in your file:')
    f.write(data + '\n')
    option=input('Do you want to continue to add more data to file:[yes|no]:')
    if option.lower()=='no':
        break
f.close()
print('Data written to the file successfully')
f=open('fname','r')
print('entered data is:',f.read())
