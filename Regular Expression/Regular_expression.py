import re
# 1. compile() function
pattern=re.compile('Python')
print(type(pattern))
# 2. finditer() function
matcher=pattern.finditer('learning python is very easy....')
# start()==> start index of the match
# end()==> end+1 index of the match 
# group()==>Returns matched string
