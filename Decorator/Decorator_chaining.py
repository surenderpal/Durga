def decor_for_f(func):
    def inner1():
        print('Decorator 1 execution')
        # func()
    return inner1
def decor2_for_f(func):
    def inner2():
        print('Decorator2 execution')
    return inner2
@decor_for_f
@decor2_for_f
def f():
    print('Originol function')
f()
