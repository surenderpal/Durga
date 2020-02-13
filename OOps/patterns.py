# n=int(input('Enter no. upto which you want to print *:'))
# print(n*'* ')
# for i in range(n):
#     print('* ', end=' ')


#WAP to print square using input num:
# n=int(input('Enter num to print square:'))
# for i in range(n):
#     print('* ' * n)

#WAP to print square using input num:
# 1 1 1
# 2 2 2
# 3 3 3
# n=int(input('Enter num to print pattern:'))
# for i in range(n): #3 = 0,1,2,3,
#     print((str(i+1)+' ')*n) 
# A A A
# B B B
# C C C 

# n=int(input('enter no for alpthabet:'))
# for i in range(n):
#     print((chr(i+ 65)+ ' ')*n)

# * 
# * *
# * * * 
# * * * * 
# * * * * *

# n=int(input('Enter no of rows:'))
# for i in range(n):
#     for j in range(i+1):
#         print('*',end=' ')
#     print()


# * * * * *
# * * * *
# * * * 
# * *
# * 

# n=int(input('Enter no. of rows:')) #n=4
# for i in range(n):                 #i=0,1,2,3
#     print('* ' * (n-i))

# pyramid                       
#           *
#         *   *
#       *   *    *
#     *   *    *   *
# SPACES= (n-i-1)
# * = (i+1)
# n=int(input('Enter no of rows:'))
# for i in range(n):
#     print(" "*(n-i-1)+'* '*(i+1))


# inverted pyramid
# space= i 
# * = (n-i)
# n=int(input('Enter no of rows:'))
# for i in range(n):
#     print(' '* i + "* "*(n-i))



# Diamond pattern
# space=
# *=
n=int(input('Enter no of rows:'))
for i in range(n):
    print(' '*(n-i-1) + ('* ' * (i+1)))
for i in range(n-1):
    print((' ' * (i+1)) + '* ' * (n-i-1))

    

