# try:
#     x=int(input('Enter first value:'))
#     y=int(input('Enter second value:'))
#     print('The result: ',x/y)
# except ZeroDivisionError:
#     print("Can't Divide with zero")
# except ValueError:
#     print('Please provide only int values only')


# try:
#     print(10/0)
# except ZeroDivisionError:
#     print('ZeroDivisionError')
# except ArithmeticError:
#     print('ArithmeticError')

try:
    print(10/0)
except ArithmeticError:
    print('ArithmeticError')
except ZeroDivisionError:
    print('ZeroDivisionError')
    