# single Inheritance=======
# class P:
#     def m1(self):
#         print('Parent class method')
# class C(P):
#     def m2(self):
#         print('Child class method')
# c=C()
# c.m1()
# c.m2()
# single Inheritance end =======
# ===========================================
# ========Multi-lvel Inheritance =========
# class P:
#     def m1(self):
#         print('parent class method.')
# class C(P):
#     def m2(self):
#         print('Child class method.')
# class CC(C):  
#     def m3(self):
#         print('Sub child class method.')
# cc=CC()
# cc.m1()
# cc.m2()
# cc.m3()
# ========Multi-lvel Inheritance End =========
#=============================================
# ========Hierachical Inheritance End =========
class P:
    def m1(self):
        print('Parent class method.')
class C1(P):
    def m2(self):
        print('Child 1 Class method.')
class C2(P):
    def m3(self):
        print('Child 2 class method.')
c1=C1()
c1.m1()
c1.m2()
c2=C2()
c2.m1()
c2.m3()
