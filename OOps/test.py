# s1= input('Enter any string:')
# i=0
# for s in s1:
#     print("character is {} and it's forward index is {} and backword index is {}".format(s,(i-len(s1)),i))
#     i+=1
# ms=input('Enter main sting:')
# ss=input('Enter sub string:')
# if ss in ms:
#     print('Subsring "{}" found in main string "{}"'.format(ss,ms))
# else:
#     print('substring "{}" is not present in the main string "{}"'.format(ss,ms))
# fs=input('Enter first sting:')
# ss=input('Enter second string:')
# if fs==ss:
#     print('Both string are equal')
# elif fs > ss:
#     print('First string is greater than second string')
# else:
#     print('Second string is greater than first string.')
# city = input('Enter city name: ').strip()
# if city == 'hyderabad':
#     print('Heloo Hyderabadi...Aadab!!')
# elif city == 'chennai':
#     print('Hello Madrasi....Vanakkam')
# elif city == 'banglore':
#     print('hello kanadiga....Namaskara')
# else:
#     print('your entered city is invalid')
# s='surender'
# print(s.find('s'))
# print(s.find('e'))
# print(s.rfind(' '))
# print(s.rfind('e'))
# print(s.rfind('e'))
# print(s.find('e',2,8))
# print(s.rfind('e',2,8))
# print(s.index('e'))
# print(s.index('x'))
# print(s.index('e',4,8))
# email=input('Enter your email-id:')
# try:
#     i= email.index('@')
#     print('mail-id contains @ which is maindatory')
# except ValueError:
#     print('Mail id is Invalid.')
# s='ABBABBBABBBABABABABAB'
# print(s.count('B',1,200))
# print(s.count('D',1,200))
# print(s.count('A'))
# print(s.count('Z'))
# s='abcabcabca'
# i=s.find('abc')
# print(i)
# i=s.find('abc',3,len(s))
# print(i)
# i=s.find('abc',6,len(s))
# print(i)
# i=s.find('abc',9,len(s))
# print(i)

# s='abcabcabcab'
# subs='abc'
# count=0
# i=s.find(subs)
# if i==-1:
#     print('Subsgring is not available!!')
# while i!=-1:
#     count+=1
#     print('{} present at index: {}'.format(subs,i))
#     i=s.find(subs,i+len(subs),len(s))
# print('Total occurance of substring {} is {}'.format(subs,count))
# s1=s.replace('a','b')
# print(s1)
# name='surender kumar pal'
# s1=name.replace(' ','',)
# print(s1)
# ts=len(name)-len(s1)
# print('Total no of spaces is {}'.format(ts))
# s='surender kumar pal'
# d='05-04-2019'
# l=d.split('-')
# print(l)
# for x in l:
#     print(x)
# l=['surender', 'kumar', 'pal']
# print(l)
# l1= "".join(l)
# print(l1)
# s='learning python is very easy'
# print("upper case:"+ s.upper())
# print("lower case:"+s.lower())
# print("swap case:"+s.swapcase())
# print("title:"+s.title())
# print("Capitalize:"+s.capitalize())

# compage two string.
# s1=input('Enter first string:').lower()
# s2=input('Enter second string:').lower()
# if s1 ==s2:
#     print("Both entered strings are equal")
# elif s1 < s2:
#     print('Entered second string "{}" is greater than first string "{}"'.format(s1,s2))
# else:
#     print('Entered First string "{}" is greater than second string "{}"'.format(s1,s2))

# login functionality.

# usrname=input('Enter your username:').lower()
# pwd=input('Enter your password:')
# if usrname =='surender' and pwd=='rahul':
#     print('Enter credentials are vaild')
# else:
#     print('Entered credentials are Invalid.')

# first and last character to uppercase and all other to lower case.
# s=input('Enter any string:')
# output=s[0].upper()+s[1:len(s)-1].lower()+s[-1].upper()
# print(output)

# s='learning python is very easy'
# print(s.startswith('learning'))
# print(s.endswith('easy'))
# print(s.startswith('lea'))
# print(s.startswith('easy'))

# Check type of character inside the string.
# print('surender1234'.isalnum())
# print('sured'.isalpha())
# print('sirmde'.isdigit())
# print('12345'.isdigit())
# print('sure'.islower())
# print('SURE'.islower())
# print('sure'.isupper())
# print('SURE'.isupper())
# print('Surender'.istitle())
# print('surender'.istitle())
# print(' surender pal'.isspace())
s=input('Enter any character:')
if s.isalnum():
    print('Alphannumeric')
    if s.isalpha():
        print('Alphabet')
        if s.isupper():
            print('Uppercase')
        else:
            print('lowercase') 
    else:
        print('digit')
elif s.isspace():
    print('space symbol')
else:
    print('special character')
