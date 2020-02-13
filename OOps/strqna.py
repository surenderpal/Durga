# reverse the given string.
# s=input('enter any string:')
# 1st method 
# print(s[::-1])
# for i in s:

# 2nd method 
# s1=reversed(s)
# for i in s1:
#     s2=''.join(s1)
#     print(s2)
# 3rd method 
# opt=''
# i=len(s)-1
# while i >=0:
#     opt=opt + s[i]
#     i=i-1
# print(opt)

# reversing string. 

# s=input('enter any string:')
# l=s.split(' ')
# print(l)  # ['python', 'is', 'very', 'easy']
# 1st method

# opt=l[::-1]
# s1=' '.join(opt)
# print(s1)

# 2nd method

# s=input('enter any string:')
# l=s.split()
# l1=reversed(l)
# for i in l1:
#     l2=' '.join(l1)
#     print(l2)

# 3rd metod
# opt=''
# i=len(s)-1
# while i >=0:
#     opt=opt + s[i]
#     i=i-1
# print(opt)
# s=input('enter string:')
# l=s.split()
# l1=[]
# i=len(l)-1
# # print(i)
# while i >=0:
#     opt=opt.append(i[::-1])
#     i=i-1
# print(opt)

#  WAP to reverse the internal contant of the string not string.
# s=input('enter string:')
# l=s.split()
# l1=[]
# for word in l:
#     l1.append(word[::-1])
# opt=' '.join(l1)
# print(opt)


# WAP to reverse the internal content of the every second word.
# s=input('enter your string:')
# l=s.split()
# l1=[]
# i=0
# while i<len(l):
#     if i%2==0:
#         l1.append(l[i])
#     else:
#         l1.append(l[i][::-1])
#     i=i+1
# opt=' '.join(l1)
# print(opt)

# WAP to merge character from two string.
# s1=input('enter first string:')
# s2=input('Enter second string:')
# i,j=0,0
# opt=''
# while i<len(s1) or j<len(s2):
#     opt=opt+s1[i] + s2[j]
#     i=i+1
#     j=j+1
# print(opt)


# s1=input('enter string:')
# s2=input('Enter string:')
# i,j=0,0
# opt=''
# while i<len(s1) or j< len(s2):
#     if i<len(s1):
#         opt=opt+s1[i]
#         i=i+1
#     if j<len(s2):
#         opt=opt+s2[j]
#         j=j+1
# print(opt)


#a4b3c5
# s='a4b3c2d1'
# opt=''
# for ch in s:
#     if ch.isalpha():
#         x=ch
#     else:
#         opt=opt+x*int(ch)
# print(opt)

#a4b3c5
# s='a5b2z4d2'
# opt=''
# for ch in s:
#     if ch.isalpha():
#         x=ch
#     else:
#         opt=opt+x*int(ch)
# ot=''.join(sorted(opt))
# print(ot)       


# s='aaaaaadddddfffrggggg'
# previous=s[0]
# opt=''
# c=1
# i=1
# while i<len(s):
#     if s[i]==previous:
#         c=c+1
#     else:
#         opt=opt+str(c)+previous
#         previous=s[i]
#         c=1
#     if i==len(s)-1:
#         opt=opt+str(c)+previous
#     i=i+1
# print(opt)


# input:  B4A1D3
# output: ABD134
# 1st way
# s='B4A1D3'
# alhpabet=[]
# digit=[]
# for ch in s:
#     if ch.isalpha():
#         alhpabet.append(ch)
#     else:
#         digit.append(ch)
# opt=''.join(sorted(alhpabet)+sorted(digit))
# print(opt)

# 2nd way
# s=input('Enter some alphanumeric string:')
# alhpabet=''
# digit=''
# for ch in s:
#     if ch.isalpha():
#         alhpabet=alhpabet+ch
#     else:
#         digit=digit+ch
# opt="".join(sorted(alhpabet)+sorted(digit))
# print(opt)


#input:a4b3c2
#output:aaaabbbcc
# s=input('Enter alphanumeric strin:')
# opt=''
# for ch in s:
#     if ch.isalpha():
#         x=ch
#     else:
#         opt=opt+x*int(ch)
# print(opt)

# input:a3z2b4a3z2
# output:aaazzbbbbzz  
# s='a3z2b4'
# opt=''
# for ch in s:
#     if ch.isalpha():
#         x=ch
#     else:
#         opt=opt+x*int(ch)
# opt=''.join(sorted(opt))
# print(opt)

# input:aaaabbbccz
# output:4a3b2c1z
# s='aaaabbbccz'
# opt=''
# previous=s[0]
# c=1
# i=1
# while i<len(s):
#     if s[i]==previous:
#         c=c+1
#     else:
#         previous=s[i]
#         opt=opt+str(c)+previous
#         c=1
#     if i==len(s)-1:
#         opt=opt+str(c)+previous
#     i=i+1
# print(opt)

# input: a4k3b2
# output:aeknbd
# s='a4k3b2'
# opt=''
# for ch in s:
#     if ch.isalpha():
#         x=ch
#         opt=opt+x
#     else:
#         n_c=chr(ord(x)+int(ch))
#         opt=opt+n_c
# print(opt)


# remove duplicate character from string
# 1st way

# s='roopasurenderpal'
# opt=''
# for ch in s:
#     if ch not in opt:
#         opt=opt+ch
# print(opt)

# 2nd way

# s='roopasurenderpal'
# opt=''
# l=[]
# for ch in s:
#     if ch not in l:
#         l.append(ch)
# opt=''.join(l)
# print(opt)

# 3rd way

# s='roopasurenderpal'
# s1=set(s)
# opt=''.join(s1)
# print(opt)

# No of occurance of each character in string using count function

# 1st way
# s='roopasurenderpal'
# l=[]
# for ch in s:
#     if ch not in l:
#         l.append(ch)
# # print(l)
# for ch in l:
#     print("{} presents {} times".format(ch,s.count(ch)))

# 2nd way
# s='roopasurenderpal'
# s1=set(s)
# print(s1)
# for ch in s1:
#     print("{} occurs {}".format(ch,s.count(ch)))

# No of occurance of each character in string without count function
# s='roopasurenderpal'
# d={}
# for ch in s:
#     d[ch]=d.get(ch,0)+1
# for k,v in sorted(d.items()):
#     print("{} occurs {} times".format(k,v))

# input:'ABAABBCA'
# output:4a3b2c1z

# s='roopasurenderpal'
# opt=''
# d={}
# for ch in s:
#     d[ch]=d.get(ch,0)+1
# for k,v in sorted(d.items()):
#     opt=opt+str(v)+k
# print(opt)

# input:'ABAABBCA'
# output: 'A4B3C1'
# s='roopasurenderpal'
# d={}
# opt=''
# for ch in s:
#     d[ch]=d.get(ch,0)+1
# for k,v in sorted(d.items()): # 
#     opt=opt+k+str(v)
# print(opt)

# no of vowel present inside the string.

# s='roopasurenderpal'
# v=['a','e','i','o','u','A','E','I','O','U']
# d={}
# for ch in s:
#     if ch in v:
#         d[ch]=d.get(ch,0)+1
# for k,v in sorted(d.items()):
#     print('{} occurs {} times'.format(k,v))

# confirm that two strings are anagram or not.
# s1= input('Enter first string:')
# s2= input('Enter second string:')
# if(sorted(s1))==(sorted(s2)):
#     print('Both strings are Anagram')
# else:
#     print("Entered string is not Anagram")


# Palindrome
# s=input('Enter string:')
# if s==s[::-1]:
#     print('Entered string is Palindrome')
# else:
#     print('Entered string is not palindrome')

# create new word by taking eachcharacter from 3 different string
s1='roopa'
s2='surender'
s3='pal'
i=j=k=0
opt=''
while i<len(s1) or j<len(s2) or k<len(s3):
    if i<len(s1):
        opt=opt+s1[i] 
        i=i+1
    if j<len(s2):
        opt=opt+s2[j] 
        j=j+1
    if k<len (s3):
        opt=opt+s3[k]
        k=k+1
print(opt)

