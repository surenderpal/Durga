class test:
    def __init__(self):
        self.__a=10     #private variable
    def __m1(self):     #private method  
        print('Private method')
    def m2(self):
        print(self.__a)
        self.__m1()
t=test()
# t.m2()
print(t.__a)
print(t.__m1())
# name mangling
# print(t._test__a)
# t._test__m1()
