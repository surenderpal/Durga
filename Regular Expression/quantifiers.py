import re
matcher=re.finditer('a$','abaabaaab')
for m in matcher:
    print(m.start(),'...',m.group())

# Quantifiers
# The number of occurrences
# a--> exactly one 'a'
# a+-> atleast one 'a'
# a*-> any number of a's including zero number also
# a?-> atmost one a
#      either one a or zero number of a's
# a{num}-> Exactly n number of a's
# ^a -> it will check whether the given string starts with a or not
# a$ -> it will check whether the given string ends with a or not
# 


