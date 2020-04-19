def decor1(func):
    def inner1():
        x=func()
        return x*x
    return inner1
@decor1
def num():
    return 20
print(num())
