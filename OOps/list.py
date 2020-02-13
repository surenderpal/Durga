# l=[]
# print(type(l))
# l.append(10)
# l.append('surender')
# l.append('roopa')
# l.append(10)
# print(l)
# dynamic input list 
# l= eval(input('Enter list:'))
# print(type(l))
# l=list('surender')
# print(l)
# print(type(l))
# l=list(range(0,10,2))
# print(l)
# print(type(l))
# s='learning python is very easy'
# l=s.split()
# print(l)
# l=[1,2,3,4]
# print(l[0])
# print(l[1])
# print(l[2])
# print(l[3])
# print(l[-1])
# print(l[100])
# l=[10,20,30,40,50,60,70,80,90,100]
# print(l[2:7])
# print(l[2:7:2])
# print(l[4::2])
# print(l[8:2:-2])
# print(l[4:100])
# print(l[4:0:2])
# print(l[::1])
# print(l[::-1])
l=[0,1,2,3,4,5,6,7,8,9,10]
# i=0
# while i<len(l):
#     print(l[i])
#     i=i+1
# for x in l:
#     print(x)

# print even no
# for x in l:
#     if x%2==0:
#         print(x)
#         # i=i+1
# l=[10,20,30,40,50,60]
# i=0
# while i<len(l):
#     print('+ve index is {} and -ve index is {} and element is {}'.format(i,i-len(l),l[i]))
#     i=i+1
    
# l1=[10,20,30]
# l2=[40,50,60]
# l3=l2*l2
# print(l3)
# l4=l1+ (1,2,3)
# print(l4)
# l1=[10,20]
# l2=[30,40]
# l3=l1+l2
# l4=l3*3
# print(l4)
# l1=['dog','cat','rat']
# l2=['dog','cat','rat']
# l3=['Dog','Cat','Rat']
# l4=['rat','dog','cat']
# print(l1==l2)
# print(l1==l3)
# print(l2==l4)
# l1=[10,20,30,40]
# l2=[50,60]
# print(l1<l2)
# print(l1<=l2)
# print(l1>l2)
# print(l1>=l2)
# l1=['ramba','ramya']
# l2=['roja','sunny']
# print(l2>l1)
# l1=[10,20,30]
# print(60 not in l1)
# l=[10,20,30,10,20,30,10]
# print(len(l))
# print(l.count(90))
# print(l.index(30))
# print(l.index(300,0,100))
# l=[10,20,30,40]
# x=int(input('enter element to find:'))
# if x in l:
#     print("{} is present at index {}".format(x,l.index(x)))
# else:
#     print("{},not present in the list".format(x))
# l=[]
# l.append(10)
# l.append(20)
# l.append(30)
# l.append(40)
# print(l)
# l.append(50)
# print(l)
#  append no divisible by 10 form 1 to 100
# l=[]
# for i in range(1,101):
#     if i%10==0:
#         l.append(i)
#         i=i+1
# print(l)
# l=[10,20,30,40]
# print(l)
# l.insert(10,100) 
# print(l)
# # print(l.index(100))
# order1=['chicken','mutton','fish']
# order2=['kf','KO','RC']
# print(order1)
# print(oxrder2)
# order1.extend(order2)
# print(order1)
# l1=[10,20,30]
# l2=[40,50]
# # l1.append(l2)
# l1.extend(l2)
# print(l1)
# print(len(l1))
# l=[10,20,30,40,50,10,10,20,10]
# print(l)
# l.remove(10)
# print(l)
# l=[1,2,3,4,5,6]
# print("Before Removal",l)
# x= int(input('Enter elements to remove:'))
# if x in l:
#     l.remove(x)
#     print("{} is removed from the list".format(x),l)
# else:
#     print("Entered element {} is not available in list".format(x),l)

# l=[1,2,1,3,4,12,1,2,1,4]
# print('Before removing duplicate values',l)
# x=int(input('Enter value to remove from the string:'))
# while True:
#     if x in l:
#         l.remove(x)
#         # print("{} is removed from the list".format(x),l)
#     else:
#         break
# print("After removal list is",l)
# l=[1,2,3]
# print("before pop method",l)
# print(l.pop())
# print("after pop method performed",l)
# print(l.pop())
# print(l.pop())
# print(l)
# print(l.pop())
# l.pop(2)
# print(l)
# l.pop(200)
# print(l)
# l=[1,2,3,4,51,2,1,12,1]
# print(l)
# print("clearing the list",l.clear())
# print(l)
# l=[1,2,3,4,5,6,7,8,9]
# print(l)
# l.reverse()
# print('reversed list',l)
# r=reversed(l)
# print(r)
# print(type(r))
# l1=list(r)
# print(l)
# s='surender'
# print(s.reverse())
# print(s)
# r=reversed(s)
# for x in r:
#     print(x)
# l=[1,2,4,5,23,12,5,8,9,0,867]
# print(l)
# l.sort(reverse=True)
# print("reverse sorted ",l)
# l=['chai','apple','banana']
# print(l)
# l.sort(reverse=True)
# print("reverse sorted ",l)
# l=[2,5,1,8,1235,123]
# l1=sorted(l)
# print(type(l1))
# print(l1)
# for x in l1:
#     print(x)
# l1=[2,3,1,5]
# # l2=l1[::]
# l2=l1.copy()
# print(l1)
# l1[1]=8888
# print("content changed",l1)
# print(id(l1))
# print(l2)
# print(id(l2))
# l=[10,20,[40,50]]
# print(l[0])
# print(l[1])
# print(l[2][0])
# print(l[2][1])

# Matrix using python
# l=[[10,20,30],[40,50,60],[70,80,90]]
# for x in l:
#     for y in x:
#         print(y,end=' ')
#     print()

# l=[]
# for x in range(1,11):
#     l.append(x)
# print(l)
# l=[x for x in range(1,11)]
# print(l)
# l=[x*x for x in range(1,11)]
# l=[x for x in range(1,11) if x%2!=0]
# l= [2**x for x in range(1,6)]
# l=[x for x in range(1,101) if x%10!=0]
# print(l)
l1=[10,20,30,40]
l2=[30,40,50,60]
# l3=[x for x in l1 if x not in l2]
# l3= [x for x in l1 if x in l2]
# l=['surender','roopa','mansi','rahul']
# l3=[x[0] for x in l ]
# s='the quick brown fox jumps over the lazy dog'
# words=s.split()
# print(words)
# l3=[[word.upper(),len(word)] for word in words]
# print(l3)
vowels=['a','e','i','o','u']
word=input('enter string:')
result=[]
# l=[[result.append(ch),len(result)] for ch in word if ch in vowels if ch not in result]
# result=[ch for ch in vowels if ch in word]
result=[ch for ch in word if ch in vowels ]
print(result)
# for ch in word:
#     if ch in vowels:
#         if ch not in result:
#             result.append(ch)
# print(result,len(result))

