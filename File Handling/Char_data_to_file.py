f=open('char.txt','a')
# f.write('Durga\n')
# f.write('Software\n')
# f.write('Solutions\n')
# f.write('Hyderabad\n')
l={'Surender\n','Rahul\n','Upika\n','Roopa\n'}
d={'surender':'sure','rahul':'g','upika':'gh'}
f.writelines(d)
f.close()
print('Data written to file successfully!!!')
