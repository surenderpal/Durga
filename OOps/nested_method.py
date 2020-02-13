class test:
    def m1(self):
        def calc(a,b):
            print('sum:',a+b)
            print('product',a*b)
            print('difference',a-b)
            print('Average',a+b/2)
            print()
        
        calc(12,24)
        calc(20,10)
        calc(40,20)
t=test()
t.m1()
