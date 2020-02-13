try:
    x=int(input('Enter first number:'))
    y=int(input('Enter second number:'))
    print("The Result:",x/y)
except (ZeroDivisionError, ValueError) as msg:
    print('The Raised Eprxception:',msg.__class__.__name__)
    print('Description of Exception:',msg)
    print('Please provide valid input only...')
