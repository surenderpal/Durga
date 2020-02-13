# super() v/s parent class instance variable
# class P:
#     a=888
#     b=30
#     def __init__(self):
#         self.b=999
# class C(P):
#     def m1(self):
#         self.b=20
#         print('parent',super().a)
#         print('child',self.b)
# c=C()
# c.m1()


#=====How to call class method and instance method from child class of parent class
# class P:
#     def __init__(self):
#         print('parent constructor')
#     def m1(self):
#         print('parent Instance method')
# class C(P):
#     @classmethod
#     def m2(cls):
#         super(C,cls).__init__(cls)
#         super(C,cls).m1(cls)
# C.m2()

# how to call parent class static & class methods from child class static method?
class P:
    @classmethod
    def m2(cls):
        print('Parent class method')
    @staticmethod
    def m3():
        print('Parent static method')
class C(P):
    @staticmethod
    def m2():
        super(C,C).m2()
        super(C,C).m3()
C.m2()
             