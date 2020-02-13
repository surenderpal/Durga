class test:
    def __init__(self):
        self.a=10
    def m1(self):
        print('Public method')
    def m2(self):
        print(self.a)
        self.m1()
t=test()
t.m2()
print(t.a)
t.m1()

