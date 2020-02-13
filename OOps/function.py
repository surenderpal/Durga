# def calculate(a,b):
#     print('sum is',a+b)
#     print('difference is',a-b)
#     print('Product is',a*b)

# # calculate(100,20)
# # calculate(20,10)
# # calculate(30,10) 

# # def wish():
# #     print('Hello friend, good Morning')
# # wish()

# def wish(name):
#     # name=input('enter your name:')
#     print("Hello",name,"good morning")
# # wish('surender')

# def square(num):
#     print('Square of entered {} is {}'.format(num,num*num))
# # square(3)

# def sum(a,b):
#     add=a+b
#     return add
# result=sum(1,2)
# # print('sum is',result)
# # print('sum is',sum(10,20))
# # def f1():
# #     print('Hello sire')
# # x=f1()
# # print('The default value of fundtion is ',x)

# # def factorial(num):
# #     fact=1
# #     while num>=1:
# #             fact=fact*num
# #             num=num-1
# #     return fact
# # f=factorial(4)
# # print(f)
# # for i in range(1,11):
# #     print('factorial of', i ,'is',factorial(i))

# # python return mulitple values at same time.

# # def sum_sub(a,b):
# #     sum=a+b
# #     sub=a-b
# #     return sum,sub

# # sum1,sub1=sum_sub(12,2)
# # print('sum of two values is:',sum1)
# # print('sub of two values is:',sub1)


# def calc(a,b):
#     sum=a+b
#     sub=a-b
#     mul=a*b
#     dev=a/b
#     return sum,sub,mul,dev
# t=calc(12,2)
# # print(t)
# # for i in t:
# #     print(i)
# # w,x,y,z=calc(12,2)
# # print(type(t))
# # print('Sum',w)
# # print('Sub',x)
# # print('mul',y)
# # print('dev',z)

# def sub(a,b):
#     print(a-b)

# # sub(100,200)# positional argument
# # sub(200,100)# positional argument
# # sub(a=100,b=200)
# # sub(b=200,a=100)
# # sub(100,b=200)
# # sub(a=100,200)


# # def wish(name='Guest'):
# #     print('Hello',name,'Good Morning!!!\nHave a great day ahead')
# # wish('surender')
# # wish(1)
# # wish()
# # print()
# # wish('surender')


# # def wish(name,msg):
# #     pass

# # def wish(name='surender',msg='Good day!!!'):
# #     pass

# # def wish(name,msg='good day!!'):
# #     pass

# # def wish(name='surender',msg):
# #     pass

# # variable length argument:
# def f1(x,*y):
#     print(x)
#     for y in y:
#         print(y)
# # f1(1,2,3,4,5,6,7)
# # f1(10)


# def f1(*x,y):
#     print(x)
#     print(y)
# # f1(1,2,3,4,5,6,7,8,9,y=323)

# def f2(x,*y):
#     print(x)
#     print(y)
    
# # f2(10)
# # f2()
# # f2(1,2,3,4,5,6,7,8,9) 
# def sum1(*n):
#     total=0
#     for x in n:
#         total=total+x
#     print('sum is: ',total)
# # sum1() 
# # sum1(13) 
# # sum1(10,20) 

# # def f1(*a):
# #     print(a)
# # f1((1,2,3,4,5),(6,7,8,9,10))

# # def f1(**kwargs):
# #     print(kwargs)
# #     print(type(kwargs))
# # f1()
# # f1(a=10,b=20)

# # def f1(*args,**kwargs):
# #     print(args)
# #     print(kwargs)
# # f1(10,20,30,a=10,b=20)


# # def f1(*kwargs,**args):
# #     print(kwargs)
# #     print(args)

# # f1(a=10, b=20,c=30,1,2,3,4,5)
# def f1(a,b,c=10,d=20):
#     print(a,b,c,d)
# # f1(2,3)
# # f1(10,20,30,40)
# # f1(25,50,d=100) # 25,50,10,100
# # f1(d=2,a=10,b=4)# syntax error kwargs should be at last.
# # f1(1,2,b=4)
# # a=10
# # def f1():
# #     print(a)
# # def f2():
# #     print(a)
# # # f1()
# # # f2()

# # def f3():
# #     a=10
# #     print(a)

# # def f4():
# #     print(a)
# # f3()
# # f4()
# # a=10
# # def f1():
# #     a=20
# #     print(a)
# # def f2():
# #     print(a)
# # f1()
# # f2()
# # a=10
# # def f1():
# #     global a
# #     a=20
# #     print(a)
# # def f2():
# #     print(a)   
# # f1()
# # f2()

# # def f1():
# #     global a
# #     a=10
# #     print(a)
# # def f2():
# #     print(a)
# # f1()
# # f2()

# a=888
# def f1():
#     global a
#     print(a)
#     a=999
#     print(a)

# # f1()
# # print(globals().get('a'))
# print(globals())
# # print(globals()['a'])

# factorial programm
# def fact(n):
#     result=1
#     while n>=1:
#         result=result*n
#         n=(n-1)
#     return result
# a=fact(4)
# print(a)=

# def fact(n):
#     if n==0:
#         result=1
#     else:
#         result=n*fact(n-1)
#     return result
# a=fact(4)
# print(a)
# for i in range(11):
#     print('Factorial of {} is: {}'.format(i,fact(i)))
    

# def squ(n):
#     print('square of entered {} is:{}'.format(n,n*n))
# squ(5)

# s=lambda n: n*n
# print(s(5))
# for i in range(1,11):
#     print('square of {} is : {}'.format(i,s(i)))
        
# s=lambda a,b: a+b
# print(s(10,20))
# bigger= lambda a,b: a if a>b else b 
# print(bigger(122,-200))
# bigger= lambda a,b,c: a if a>b and a>c else b if b>c else c
# print(bigger(3.0,3.1,3.11))

# l=[0,1,2,3,4,5,6,7,8,9,10]
# def is_even(n):
#     if n%2==0:
#         return True
#     else:
#         return False
# l1=[]
# for n in l:
#     if is_even(n)==True:
#         l1.append(n) 
# l1=[]
# def is_even(n):
#     if n%2==0:
#         return True
#     else:
#         return False
# for n in l:
#     if is_even(n)==True:
#         l1.append(n)  
# print(l1)
# l=[0,1,2,3,4,5,6,7,8,9,10]
# def is_even(n):
#     if n%2==0:
#         return True
#     else:
#         return False
# l1=list(filter(is_even,l))
# print(l1)
# s=lambda n: True if n%2==0 else return False 
# print(s)
# l=[0,1,2,3,4,5,6,7,8,9,10]
# l1=list(filter(lambda n:n%2==0,l))
# print('even no',l1)
# odd=set(filter(lambda n: n%2!=0,l))
# print('odd no',odd)
# nby3odd=list(filter(lambda n: n%3==0 and n%2!=0,l))
# print('factor of 3 and odd no.',nby3odd)
heroines=['katrinakaif','kareenakapoor','anushka','deepika','sunnyleone','mallika']
# starwithk=list(filter(lambda name: name[0]=='k',heroines ))
# print(starwithk)
# lengthby5=list(filter(lambda name: len(name)%5==0,heroines))
# print(lengthby5)
# namelenodd=list(filter(lambda name: len(name)%2!=0,heroines))
# print(namelenodd)
# l=[0,1,2,3,4,5,6,7,8,9,10]
# def is_even(n):
#     if n%2==0:
#         return True
#     else:
#         return False
# l1=list(filter(is_even,l))
# print(l1)
# l2=[]
# def starwithk(name):
#     if name[0]=='k':
#         return True
#     else:
#         return False
# for name in heroines:
#     if starwithk(name)==True:
#         l2.append(name)
# print(l2)
l=[1,2,3,4,5,6,7,8,9]
# sq=list(map(lambda n: n*n,l))
# print(sq)
# l2=[5,10,15,20,25]
# l3=list(map(lambda a,b:a*b,l,l2))
# print(l3)
# l2=[1,2,3,4,5,6,7,8,9,10]
# l3=[1,2,3,4,5]
# add=list(map(lambda a,b,c:a+b+c,l,l2,l3))
# print(add)
from functools import reduce
# result=reduce(lambda a,b: a+b,l)
# print(result)
result=reduce(lambda x,y:x+y,range(1,101))
print(result)
