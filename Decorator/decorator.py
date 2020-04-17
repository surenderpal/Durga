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

def outer():
    def inner():
        print('Inner function execution..')
    return inner    
outer()
f1=outer()
f1()
