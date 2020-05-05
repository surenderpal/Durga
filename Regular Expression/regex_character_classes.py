# [abc]= either a or b or c
# [^abc]= except a and b and c
# [a-z]= Any lower case alphabet symbols
# [A-Z]= Any upper case alphabet symbols
# [a-zA-Z]=Any alphabet symbol
# [0-9]= any digit
# [a-zA-Z0-9]=Any alphanumeric character
# [^a-zA-Z0-9]=Except any alhpanumeric character i.e special characters
import re
matcher=re.finditer('.','a7b @k9z')
for m in matcher:
    print(m.start(),'...',m.group()) #group method returns the matched item
# Prdefined character classes
# \s--> space character 
# \s--->Except space chatacter
# \d--> any digit [0-9]
# \D--> Except any digits [^0-9]
# \w--> Any word chatacter(Alphanumeric character)[a-zA-Z0-9]
# \W--> Except any alphanumeric character(special character)[^a-zA-Z0-9]
# . --> Every character
