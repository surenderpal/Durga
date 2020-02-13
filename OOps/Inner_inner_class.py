class outer:
    def __init__(self):
        print('outer class object creation...')
    class inner:
        def __init__(self):
            print('Inner class object creation...')
        class inner_inner:
            def __init__(self):
                print('Inner_inner object creation....')
            @staticmethod
            def m1():
            # def m1(self):
                print('Nested Inner class static-method')
                # print('Nested Inner class method')                
o=outer()
i=o.inner()
# ii=i.inner_inner()
# ii.m1()
# outer().inner().inner_inner().m1()
m=i.inner_inner.m1()
