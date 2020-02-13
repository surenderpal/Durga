# t=(10,'surender',10.78,3)
# print(type(t))
# print(t)
# t1=10,'surender',10.78,3
# print(t1)
# print(type(t1))
# print(t[1])
# print(t[-1])
# l=[10,20,30]
# print(l)
# l[0]=999
# print(l)

# t=(10,203,30,40)
# print(t)
# t[1]=2222
# print(t)
# t=()
# print(type(t))

# empty tyupel
# t=()
# print(type(id))

# single valued tuple
# t=(10,)
# print(type(id))
# t=10,
# print(type(id))

# multi valued tuple
# t=(10,20,39,)
# print(type(t))
# t=(10,20,39)
# print(type(t))
# l=[23.4,'siremder',34]
# t= tuple(l)
# print(type(t))
# print(t)
# t=tuple(range(1,11,2))
# t=tuple('surender')
# print(t[1])
# t=input('Enter tuple vales:')
# print(type(t))
# s='surender'
# s=[10,290,30]
# s=(10,20,304,505,647,7,47,4567)
# print(s[10])
# t1=(10,20,30)
# t2=(40,50,60)
# t3=t1+t2
# print(t3)
# t1=(10,20)
# t2=3* t1*3
# print(t2)
# t1=('cat','rat','dog')
# t2=('cat','rat','dog')
# t3=('dog','cat','rat')
# t4=('Cat','Rat','Dog')
# print(t1==t1)
# print(t2==t3)
# print(t2==t4)
# t1=(10,20,30,10,2000,10)
# t2=(40,50,60)
# print(t1<t2)
# print(t1>t2)
# print(10 in t1)
# print(100 not in t2)
# print(len(t1))
# print(t1.count(10))
# t=(10,20,30)
# r=reversed(t)
# t1=tuple(r)
# print(r)
# print('Original tuple:',t)
# print('Reversed tuple:',t1)
# t=(20,5,10,15,0)
# print(t.sort())
# l=sorted(t,reverse=True)
# t2=tuple(l)
# print('Original tuple:',t)
# print('Reversed tuple:',t2)
# print("Max elemtnt: ",max(t))
# print("Min element: ",min(t))
# a=10
# b=20
# c=30
# d=40
# t=(10,20,30,40)
# t=a,b,c,d
# l=[a,b,c,d]
# print(t)
# print(l)
# a,b,c,d=t
# print(a,b,c,d)
# a,*b=t
# print(a)
# print(b)
# t=(x*x for x in range(1,11))
# print(type(t))
# import collections
# s={10,20,30}
# l=[10,30,40]
# t=(10,20,30)
# print(isinstance(l,collections.Hashable))
# print(isinstance(t,collections.Hashable))
# print(hash(t))
# print(hash(l))
# s.add(t)
# print(s)
# s.add(l)
# print(s)
t=eval(input('Enter tuple of numberes:'))
# sum=0
# for x in t:
#     sum=sum+x
# print('Sum of number is:',sum)
# print('Average of number is:',sum/len(t))
print('Sum of number is:',sum(t))
print('Average of number is:',sum(t)/len(t))
