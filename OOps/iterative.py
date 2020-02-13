# s=input("Enter any string:")
# i=0
# for x in s:
#     print('the character present at {} index is {}'.format(i,x))
#     i+=1

# s="welcome to the for loop:"
# for x in range(1,11):
#     print("Repeating string @ {} times:{}".format(s,x))


# display odd number from 0 t0 20:

# odd_num=[]
# for x in range(0,21):
#     if x%2!=0:
#         print(x)

# odd no. using list

# odd_list=[]
# for x in range(0,21):
#     if x%2!=0:
#         odd_list.append(x)
# print("Odd elements in range from 0 to 20 are:", odd_list)

# odd no. using set
# set1=set()
# for x in range(0,21):
#     if x%2!=0:
#         set1.add(x)
# print("Odd elements in range from 0 to 20 are:", set1)


# decrement value from 10 t o 1:

# for x in range(10,0,-1):
#     print(x)


# sum of elements in the list
# l=eval(input('enter list of no.'))
# sum=0
# for x in l:
#     sum+=x
# print("sum is:",sum)
# print(sum(l))

# hello msg 10 times using for loop:

# for x in range(1,11):
#     print("hello time {}".format(x))

# hello msg 10 times using for while:

# i=1
# while i<=10:
#     print('hello to world while loop:{}'.format(i))
#     i=i+1


# print num using for:
# for i in range(1,11):
#     print(i)
#     i=i+1


# print num using while:

# i=1
# while i<=10:
#     print(i)
#     i=i+1

# print num from 1 to 20 divislbe by 3:

# for x in range(1,21):
#     if x%3==0:
#         print(x)
#     x=+1

# x=1
# while x<=20:
#     if x%3==0:
#         print(x)
#     x=x+1


# print sum of first 'n' numbers
# n=int(input('Enter no:'))  
# sum=0
# i=1
# while i<=n:
#     sum=sum+i
#     i=i+1
# print('Sum is:',sum)

# sum=0
# i=1
# n=int(input('enter num:'))      
# for x in range(n):
#     if i<=n:
#         sum=sum+i
#         i=i+1
# print('sum is',sum)


# name=input('Enter your name:')
# name=''
# while name!='surender':
#     name=input('Enter you favorite actress:')
# print('Thanks for confirmation!!')


#infinite loops:

# i=1
# while True:
#     print('Hello world',i)
#     i=i+1

#nested loops:
# for i in range(3):
#     for j in range(2):
#         print('hello world {}'.format(j))

for i in range(3):
    for j in range(2):
        print('i={},j={}'.format(i,j))
