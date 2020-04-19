def decor_for_f(func):
    def inner1():
        print('Decor 1 execution')
        # func()
    return inner1
def decor2_for_f(func):
    def inner2():
        print('Decor 2 execution')
        f()
    return inner2
@decor2_for_f    
@decor_for_f
def f():
    print('Original function')
f()
