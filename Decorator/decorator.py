#function aliasing
# def wish(name):
    # print('Good Morning,',name)
# greeting=wish
# del wish #deleting one referance variable but we can access the function using second variable
# print(id(wish))
# print(id(greeting))
# wish('surender')
# greeting('surender')

#================================ Nested function
# def outer():
#     print('outer function execution started')
#     def inner():
#         print('Inner funciton execution')
#     # inner()# calling inside of outer funciton 
#     print('outer function execution completed')
#     # inner() #calling end of outside function
# outer()
# function as return value
# def outer():
#     def inner():
#         print('Inner function execution..')
#     return inner    
# outer()
# f1=outer()
# f1()

# # function as argument
# def f1(func):
#     func()
# def f2():
#     print('f2 function')
# f1(f2)

l=[1,2,3,4,5,6,7,8,9,10]
def is_even(n):
    if n%2==0:
        return True
    else:
        return False
l2=list(filter(is_even,l))
print(l2)
