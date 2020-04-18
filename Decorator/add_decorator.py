def decor_for_add(func):
    def inner(a,b):
        print('#'*30)
        print('The sum is ',end= '')
        func(a,b)
        print('#'*30)
    return inner
@decor_for_add
def sum(a,b):
    print(a+b)
sum(10,20)
