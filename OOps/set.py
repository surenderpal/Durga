# s={}
# s=set()
# print(type(s))ß
# s.add(10)
# s.add(23)
# s.add(43)
# s.add(234)
# s.add(10)
# print(s)
# print(s[0])
# print(s[::])
# s=set() # empty set
# print(type(s))
# s.add(1)
# s.add(23.44)
# s.add('A')
# print(s)
# st={10,20,30,'A',10.233,10}
# print("Declared with data:",st)
# l=[10,20,30.90,10,33]
# sp=set(l)
# print('list converted to set:',sp)
# s=set(range(0,11,2))
# print('Range inside set',s)
# s=set('apple')
# print(s)
# s=eval(input('Enter set of values:'))
# print(s)
# print(type(s))
# s1={10,20,30}
# s2={30,20,10}
# s3=s1+s2
# s4=s1*3
# print(s4)
# print(s1==s2)
# print(s1==s2)
# s1={10,20,30}
# s2={20,10,40,50,60}
# print(s1<s2)
# print(s1>s2)
# print(s1<=s2)
# print(10 in s1)
# print(100 not in s2)
# print(len(s2))
# s={20,10,40,50,60}
# s.add(100)
# print(s)
# s1={1.2,3.4,5.6}
# s2={'surender','roopa','pal'}
# s.update(s1,s2)
# print(s)
# s.update(range(200,211),'ramlakhan')
# print(s)
# s={10,20,30,40,50}
# print('Before removing',s)
# s.remove(10)
# print('After removing',s)
# s.remove(100)
# s.discard(50)
# print('After removing',s)
# s.discard(190)
# print(s.pop())
# print(s.pop())
# print(s.pop())
# print(s.pop())
# print(s.pop())
# print(s.pop())
# s.clear()
# print(s)
s1={10,20,30,40}
s2={30,40,50,60}
# s3=s1.union(s2)
# s3=s1|s2
# s3=s1.intersection(s2)
# s3=s1 & s2
# s3=s1.difference(s2)
# s3=s1.symmetric_difference(s2)
# print(s3)
s3=s1
# print('alising:',s3)
# s1.pop()
# print('before pop s1',s1)
# print('after pop s3',s3)
# s3=s1.copy() #cloning
# s1.pop()
# print(s3)
# s={x*x for x in range(1,6)}
# s={2**x for x in range(1,6)}
# print(s)
# print(type(s))
l=[10,10,20,30,20,10,30]
# s=set(l)
# l1=list(s)
# print(l1)
# l1=[]
# for x in l:
#     if x not in l1:
#         l1.append(x)
# print('duplication removed:',l1)
# print('origional list:',l)
word=input('Enter string for search vowel:')
s=set(word)
v={'a','e','i','o','i','u'}
# s1=s.intersection(v)
s1=s & v
print('vowels in string:',s1)
