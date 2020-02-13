class outer:
    def __init__(self):
        print('Outer class object creation')
    class inner:
        def __init__(self):
            print('Inner class object creation')
        def m1(self):
            print('Inner class method')
# o=outer()
# i=inner()
# i=outer().inner()
# i=o.inner()
# i.m1()
i=outer().inner().m1()
print(type(i))
