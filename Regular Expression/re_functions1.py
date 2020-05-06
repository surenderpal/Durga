# function finditer()
import re
# matcher=re.finditer('\D','12dsafd43 q434eq')
# for m in matcher:
#     print(m.start(),'...',m.end(),'...',m.group())

# function sub()
# substitution or replacement
# re.sub(regex,replacement,targetstring)
# s=re.sub('\d','@','s12ure234nde324r')
# print(s)

# function subn()
# how many replacement happen i.e number 
# s=re.subn('\w','@','surenderpal')
# print('Result String is:',s) # it will return entire tuple 
# print('Result String is:',s[0])
# print('The Number of replacements:',s[1])

# function split()
l=re.split('-','1-2-3-4-5-6')
l=re.split('\.','www.surenderpal.com')
print(l)
