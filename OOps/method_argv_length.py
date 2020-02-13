# how to define a method with variable number of arguments
# 1)Method with Default arguments

# class Test:
#     def m1(self,a=None,b=None,c=None):
#         if a is not None and b is not None and c is not None:
#             print('Three-arguments method')
#         elif a is not None and b is not None:
#             print('Two-arguments method')
#         elif a is not None:
#             print('One-argument method')
#         else:
#             print('No-argument method')
# t=Test()
# t.m1()
# t.m1(2)
# t.m1(1,2)
# t.m1(1,2,3)

# 2)method with Variable number of Arguments
# class Test:
#     def m1(self,*args):
#         print('Method with variable length arguments')
# t=Test()
# t.m1()
# t.m1(1)
# t.m1(1,2)
# t.m1(1,3,3)
# t.m1(1,3,4,45,5,4)

# sum method with variable length of argument
class Test:
    def sum(self,*args):
        total=0
        for ele in args:
            total=total+ele
        print('Total is ',total)
t=Test()
t.sum()
t.sum(1)
t.sum(1,2)
t.sum(1,2,3,4,5,6,6,6,7,7)
