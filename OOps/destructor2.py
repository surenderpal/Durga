import time
class test:
    def __init__(self):
        print('Constructor execution..')
    def __del__(self):
        print('Destructor execution...')
t1=test()
t2=t1
t3=t1
del t1
time.sleep(10)
print('Object not destroyed after deleting T1')
del t2
time.sleep(10)
print('Object not destroyed after deleting T2')
time.sleep(10)
print('Removing last reference...')
del t3
time.sleep(10)
print('End of application.....')
