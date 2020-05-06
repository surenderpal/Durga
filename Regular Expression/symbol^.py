import re
# ^ symbol means start with
s='Learning python is very easy'
# res=re.search('^Learn',s)
# if res!=None:
#     print('Target string stars with Learn')
# else:
#     print("Target string doesn't start with Learn")

# $ symbol means ends with
res=re.search('Easy$',s,re.IGNORECASE)
if res!=None:
    print("Target string end with easy")
else:
    print("Target string doesn't end easy")
