class P:
    def m1(self):
         print('parent method')
class C(P):
    def m1(self):
        super().m1()
        print('Child mehtod')
c=C()
c.m1()
#===================
class P:
    a=10
    def __init__(self):
        print('Parent Construcor')
    def m1(self):
        print('Parent Instance method')
    @classmethod
    def m2(cls):
        print('Parent Class method')
    @staticmethod
    def m3():
        print('Parent Static method')
class C(P):
    def __init__(self):
        print('Child constructor')
    def method1(self):
        print(self.a)
        self.m1()
        self.m2()
        self.m3()
        super().__init__()
c=C()
c.method1()
