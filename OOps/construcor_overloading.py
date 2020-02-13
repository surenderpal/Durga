# class Test:
#     def __init__(self):
#         print('No arg constructor')
#     def __init__(self,x):
#         print('One arg constructor')
#     def __init__(self,x,y):
#         print('Two arg constructor')
# t=Test(19,2)


# how to define a constructor with variable number of arguments
# 1)Constructor with Default arguments

# class Test:
#     def __init__(self,a=None,b=None,c=None):
#         print('Constructor with 0|1|2|3 Arguments')
# t=Test()
# t=Test(2)
# t=Test(2,4)
# t=Test(3,4,5)

# 2)Constructor with Variable number of Arguments
class Test:
    def __init__(self,*args):
        print('Constructor with variable length of arguments')
t=Test()
t=Test(1)
t=Test(1,2)
t=Test(1,3,4,2,5,4,35,35,53,53,53,43)
 





