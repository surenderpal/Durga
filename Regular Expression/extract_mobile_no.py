import re
f1=open('input.txt','r')
f2=open('output.txt','w')
for line in f1:
    l=re.findall('[6-9]\d{9}',line)
    for number in l:
        f2.write(number+'\n')
print('Extracted all mobile number in Output.txt file')
f1.close()
f2.close()
 