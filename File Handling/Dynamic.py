fname=print('enter file name:')
f=open('fname','w')
while True:
    data=input('Enter data to write in your file:')
    f.write(data+'\n')
    option=input('Do you want to continue to add more data to file:[yes|no]:')
    if opion.lower()=='no':
        break
print('Your data that you have entered in the file is:')
f.close()
