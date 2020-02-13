class P:
    def __init__(self):
        print('parent constructor')
    def m1(self):
        print('Parent Instance method')
    @classmethod
    def m2(cls):
        print('Parent class method')
    @staticmethod
    def m3():
        print('Parent static method')
class C(P):
    def __init__(self):
        super().__init__()
        super().m1()
        super().m2()
        super().m3()
        print()
    def m1(self):
        super().__init__()
        super().m1()
        super().m2()
        super().m3()
        print()
    @classmethod
    def m2(cls):
        super().__init__()
        super().m1()
        super().m2()
        super().m3() 
        print()
    @staticmethod
    def m3():
        # super().__init__()
        # super().m1()
        # super().m2()
        # super().m3()
        print()
# c=C()
# c.m1()
C.m3()
# c.m3()

