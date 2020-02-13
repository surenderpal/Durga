class A:
    # pass
    def m1(self):
        print(' A Class method ')
class B:
    # pass
    def m1(self):
        print(' B Class method ')
class C:
    # pass
    def m1(self):
        print(' C Class method ')
class D(A,B):
    # pass
    def m1(self):
        print(' D Class method ')
class E(B,C):
    # pass
    def m1(self):
        print(' E Class method ')
class F(D,E,C):
    # pass
    def m1(self):
        print(' F Class method ')
f=F() 
f.m1()
print(F.mro())

