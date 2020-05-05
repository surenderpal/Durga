import re
pattern=re.compile('ab')
matcher=re.finditer('ab','abaababa')
print(type(matcher))
count=0
for match in matcher:
    count+=1
    print('Start Index:{}, End Index:{}, Group Index:{}'.format(match.start(),match.end(),match.group()))
print('No of occurances:',count)
