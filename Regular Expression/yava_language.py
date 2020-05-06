# 1.The allowed characters are:
#   alphabets
#   digits
#   #

# 2. First character should be lower case alphabet symbol from a to k

# 3. The second character should be any digit divisible by 3
#    [0369] [3690]
# 4. The length of identifier should be atleast 2

# [a-k][3690][a-zA-Z0-9#]*  
import re
s=input('Enter identifier to validate:')
m=re.fullmatch('[a-k][3690][a-zA-Z0-9#]*',s)
if m!=None:
    print(s,'is valid yava Identifier')
else:
    print(s,'is Invalid yava Identifier')
