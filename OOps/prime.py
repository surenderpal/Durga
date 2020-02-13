#check entered no is prime or not.

# n=int(input('Enter Number: '))
# if n<=1:
#     print('Entered no is not prime, enter greater than 1')
# else:
#     is_prime = True
#     for i in range(2,n//2+1):
#         if n%i ==0:
#             is_prime = False
#             break
#     if is_prime == True:
#         print('Entered num {} is prime '.format(n))
#     else:
#         print('Entered num {} is not prime '.format(n))

# Check that wether no entered no is prime or not.
n=int(input('enter any value:'))
n1=2
while n1<=n:
    is_prime=True
    for i in range(2,n1//2+1):
        if n1 % i ==0:
            is_prime = False
            break
    if is_prime == True:
        print(n1)
        n1=n1+1

