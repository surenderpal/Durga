# validate mobile no is valid or not
import re
s=input('Enter mobile no to validate:-')
m=re.fullmatch('[6-9]\d{9}',s)
if m!= None:
    print(s,'Mobile no is valid')
else:
    print(s,'Mobile no is Invalid')
