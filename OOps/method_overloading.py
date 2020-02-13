class Test:
    def m1(self,x):
        print('{}- type method'.format(x.__class__.__name__))
t=Test()
t.m1(10)
t.m1(3.24)
t.m1('surender')
