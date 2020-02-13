# print('statement 1')
# try: 
#     print(10/0)
# except ZeroDivisionError:
#     print(10/2)
# print('statement 3')

# try:
#     print(10/0)
# except ZeroDivisionError as msg:
#     print('Exception type:',type(msg))
#     print('Exception type:',msg.__class__)
#     print('Exception class name :',msg.__class__.__name__)
#     print('Exception description:',msg)

try:
    x=int(input('Enter first number:'))
    y=int(input('Enter second number:'))
    print('The result:',x/y)
except BaseException as msg:
    print('Type of exception is:',type(msg))
    print('Type of exception is:',msg.__class__)
    print('Name of exception is:',msg.__class__.__name__)
    print('Description of exception is:',msg)
