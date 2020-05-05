import re
pattern=re.compile('ba')
matcher=pattern.finditer('abaababa')
count=0
for match in matcher:
    count+=1
    print('Match is available at start index:',match.start())
    print('Match is available at end index:',match.end()-1)
    print('Match is available at Group:',match.group())
    print('Total match count is:',count)
