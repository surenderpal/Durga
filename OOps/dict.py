# d={100:'surender','A':300,200:'Rahul','B':400,100:'Roopa'}
# print(d)
# l=[(100,'A'),(200,'B'),(300,'C')] #list of tuple
# l=[[100,'A'],[200,'B'],[300,'C']] #list of list
# l=[{100,'A'},{200,'B'},{300,'C'}] #list of set
# l={[100,'A'],[200,'B'],[300,'C']} #set of list--not work
# l={{100,'A'},{200,'B'},{300,'C'}} #set of set--not work
# l={(100,'A'),(200,'B'),(300,'C')} #set of tuple
# l=([100,'A'],[200,'B'],[300,'C']) #tuple of list
# l= ({100,'A'},{200,'B'},{300,'C'}) #tuple of set
# l={{100,'A'},{200,'B'},{300,'C'}} #tuple of typel--not work 
# d=dict(l)
# d=eval(input('Enter any dict:'))
# print(d)
# print(type(d))
# d={100:'surender',200:'rahul',300:'roopa'}
# print(d[100])
# print(d[200])
# print(d[300])
# print(d[400])
# print(d[100])
# key=eval(input('Enter key to access the value of dict: '))
# if key in d:
#     print(d[key])
# else:
#     print('Enter correct key')
# d={100:'surender',200:'rahul',300:'roopa'}
# print(d)
# d[400]='mansi'
# print(d)
# d[200]='mature'
# print(d)
# del d[100]
# print(d)
# del d[300],d[200]
# print(d)
#WAP to print name and marks of student input using keyboard.
# n=int(input('Enter how many students are there:'))
# d={}
# for i in range(n):
#     name=input('Enter student name:')
#     marks=int(input('Enter student marks:'))
#     d[name]=marks
# print('*'*30)
# print('Name','\t\t','Marks')
# print('*'*30)
# for name in d:
#     print(name,'\t\t',d[name])
# d1={100:'a',200:'b'}
# d2={300:'c',400:'d'}
# d3=d1+d2
# d3=d1*2
# print(d1==d2)
# d3={200:'b',100:'a'}
# print(d1==d3)
# print(d1<d2)
# print(d1>d2)
# print(100 in d1)
# print(300 in d1)
# print('a' not in d1,'lol')
# Methods functions for dictionary
# d={100:'a',200:'b',300:'c',400:'d',500:'f'}
# print(len(d))
# print(d.get(700))
# print(d.get(400))
# print(d.get(700,'ket not available'))
# print(d[700])
# print('before update',d)
# d1={700:'g',800:'h'}
# d.update(d1)
# print('after update',d)
# k=d.keys()
# print(k)
# print(type(k))
# for key in k:
#     print(key)
# print(type(key))
# v=d.values()
# print(v)
# print(type(v))
# for values in d.values():
#     print(values)
# print(type(values))
# i=d.items()
# print(i)
# print(type(i))
# for item in i:
#     print(item)
# print(type(item))
# for k,v in d.items():
#     print(k,'.....',v)
# WAP to find the values from the dictionary

# d={100:'a',200:'b',300:'c',400:'d',500:'f'}
# k=d.keys()
# # print(k)
# key=int(input('Enter key to find value in dict:'))
# if key in d:
#     print('value of given key is:',format(d.get(key)))
# else:
#     print('key is not present insdie the "dict"')


# WAP to find the key from the dictionary

# d={100:'a',200:'b',300:'c',400:'d',500:'f'}
# values=input('Enter values to search key in dictionary:')
# available=False
# for k,v in d.items():
#     if v==values:
#         print('Corresponding key is ',k)
#         available=True
# if available==False:
#         print('corresponding key is not present')

# d={100:'a',200:'b',300:'c',400:'d',500:'e'}
# print('before pop',d)
# print(d.pop(900,'default value'))
# print('after pop',d)
# print(d)
# print(d.popitem())
# print(d.popitem())
# print(d.popitem())
# print(d.popitem())
# print(d.popitem())
# print(d.popitem())
# d.clear()
# print(d)
# set default()
# d={100:'a',200:'b',300:'c',400:'d',500:'e'}
# print('before setdefault:',d)
# print(d.setdefault(900,'surender'))
# print('after setdefault:',d)
# print('SetDefault',d.setdefault(100,"Surender"))
# d1={100:'a',200:'b'}
# d2=d1
# d1[300]='c'   # aliasing
# print(d1)
# print(d2)
# d2=d1.copy()    #cloning
# d1[300]='c'
# print(d1)
# print(d2)

# WAP to take dict from keyboard and print sum of values
# d=eval(input('Enter values for dict:'))
# sum=0
# for item in d.items():
#     sum=sum+item[1]
# print('Sum of values in dict',sum)
# print('Sum of values present inside the dict is ',sum(d.keys()))


#WAP to find the occurance of each letter present in the given string.
# word=input('Enter string to find occurance of each word:')
# d={}
# for ch in word:
#     d[ch]=d.get(ch,0)+1
# for k,v in d.items():
#     print(k,'....',v)

# WAP to find number of vowels present inside the string

# word=input('enter string:')
# d={}
# vowels={'a','e','i','o','u'}
# for ch in word:
#     if ch in vowels:
#         d[ch]=d.get(ch,0)+1
# for k,v in sorted(d.items()):
#     print(k,'occurs',v,'times')

# WAP to accept student name and marks from the keyboard and display student name and marks
# n=int(input('Enter how many students you want to enter:'))
# d={}
# for i in range(n):
#     name=input('enter student name:')
#     marks=input('enter student marks:')
#     d[name]=marks
# print('Insertion is completed....')
# print('*'*30)
# print('NAME','\t\t','MARKS')
# print('*'*30)
# for k,v in d.items():
#     print(k,'\t\t',v)
# print('Search operation started...')
# while True:
#     name=input('Enter student name to get marks:')
#     marks=d.get(name,-1)
#     if marks==-1:
#         print('Student not found....')
#     else:
#         print('Entered student ',name,'got marks',marks)
#     option=input('Do you want to find out another student marks(yes/no):')
#     if option=='No':
#         break
# print('Thanks for using our application....')

# Dict comprehension
# d={x:x*x for x in range(1,6)}
d={x:2**x for x in range(1,6)}
# print(d)
for k,v in d.items():
    # print(k,'square is',v)
    print('"2" power of',k,"is",v)
