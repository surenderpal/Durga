# class parent:
#     def m1(self):
#         print('Parent object created...')
# class child(parent):
#     def m2(self):
#         print('Child object created...')
# c=child()  
# c.m1()
# c.m2()

# =====Lazy child example=====
class P:
    a=10
    def __init__(self):
        print('Parent constructor......')
        self.b=20
    def m1(self):       #Instance method
        print('Parent instance method...')
    @classmethod
    def m2(cls):
        print('Parent class method......')
    @staticmethod
    def m3():
        print('Parent static metod......')
class C(P):
    pass

c=C()
# print(c.a)
# print(c.b)
# c.m1()
# c.m2()
# c.m3()
