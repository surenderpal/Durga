import sys
class test:
    pass
t=test()
t1=t
t2=t1
t3=t2
del t3,t2
print(sys.getrefcount(t))

