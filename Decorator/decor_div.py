def decor_for_devision(func):
    def inner(a,b):
        if b ==0:
            print('#'*50)
            print("Hello Stupid, How we can divide with Zero, you idiot !!!")
            print('*'*50)            
        else:
            func(a,b)
    return inner
@decor_for_devision
def devision(a,b):
    print(a/b)
devision(10,2)
devision(10,0)
devision(12,6)
devision(0,0)
