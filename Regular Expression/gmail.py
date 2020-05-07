import re
s=input('Enter mail id:')
# m=re.fullmatch('\w[a-zA-Z0-9_.]*@(gmail|rediffmail)[.][a-z]+',s)
m=re.fullmatch('\w[a-zA-Z0-9_.]*@[a-z0-9]*[.][a-z]+',s)

if m!= None:
    print('Entered E-mail Id is Valid')
else:
    print('Entered E-mmail is Invalid')
