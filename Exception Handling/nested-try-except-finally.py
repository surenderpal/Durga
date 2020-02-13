try:
    print('Outer Try Blcok')
    print(10/0)
    try:
        print('Inner Try Block')
        # print(10/0)
    # except ZeroDivisionError:
    except ValueError:    
        print('Inner Except block')
    finally:
        print('Inner Finally block')
except:
    print('Outer except block')
finally:
    print('Outer finally block')
