# How to call method of a particular Super Class
class A:
    def m1(self):
        print('A class method')
class B(A):
    def m1(self):
        print('B class method')    
class C(B):
    def m1(self):
        print('C class method')
class D(C):
    def m1(self):
        print('D class method')
class E(D):
    def m1(self):
    #     print('E class method')
        # super().m1()
        # B.m1(self)====First method to call particular class
        super(D,self).m1()
e=E()
e.m1()# E class method
# super().m1()    #D class method


