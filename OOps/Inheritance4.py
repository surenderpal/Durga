# class P1:
#     def m1(self):
#         print('Parent 1 method...')
# class P2:
#     def m2(self):
#         print('Parent 2 method...')
# class C(P1,P2):
#     def m3(self):
#         print('Child class method')
# c=C()
# c.m1()
# c.m2()
# c.m3()

#=====Diamond Access problem======
class P1:
    def m1(self):
        print('Parent 1 method..')
class P2:
    def m1(self):
        print('Parent 2 method..')
# class C(P1,P2):
class C(P2,P1):
    pass
c=C()
c.m1()
