# ============some important functions in Regular expression========
# 1. match() ====> to check the given pattern at the begning of the target string, If then returns Match object otherwise return None
# 2. fullmatch() ==> complete string should be matched, otherwise it will return None  
# 3. search() ===> search the given string , return match object of the first occurrence otherwise returns None
# 4. findall()
# 5. finditer()
# 6. sub()
# 7. subun()
# 8. split()
# 9. compile()
import re
# s=input('Enter pattern to check:')
# # m=re.match(s,'surender pal')
# m=re.fullmatch(s,'surender pal')
# if m!=None:
#     print('Full string matched.')
#     # print('Match is available at the begning of the string')
#     # print('Start Index {} and End Index {}'.format(m.start(),m.end()))
# else:
#     # print('Match is not available at the begning of the string.')
#     print('Full string not matched.')

# search
# s=input('Enter pattern to check:')
# m=re.search(s,'abaabaaab')
# if m!=None:
#     print('Match is available.')
#     print('First occurrence with start index {} and end index {}'.format(m.start(),m.end()))
# else:
#     print('Match is not available')


# find all

l=re.findall('[0-9]','a7b9k6z')
print(l)
