f=open('linux_basic_code.txt','r+')
# f.read()
f.write('hello this is my first line\n')
f.write('hello this is my second line\n')
f.write('hello this is my third line\n')
f.write('hello this is my fourth line\n')
l=['sureder','pal' 'is' 'going' 'to' 'become' 'Data Scientist\n']
d={'1':'surender','2':'roopa','3\n':'pal\n'}
# f.writelines(d)
f.writelines(l)
# print('file Name:',f.name)
# print('file mode:',f.mode)
# print('Wether file is closed:',f.closed)
# print('Weather file is readable:',f.readable())
# print('Weather file is writable:',f.writable())
# f.writelines(d['2'])
f.writelines(d.values())
f.close()

