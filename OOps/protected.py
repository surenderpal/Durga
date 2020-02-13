class test:
    def __init__(self):
        self._a=10
    def m1(self):
        print('protected method')
        print(self._a)
class subtest(test):
    def m2(self):
        print(self._a)
t=subtest()
t.m1()
t.m2()
print(t._a)

