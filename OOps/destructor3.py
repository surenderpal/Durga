import time
class test:
    def __init__(self):
        print('constructor created...')
    def __del__(self):
        print('destructor created....')
l=[test(),test(),test()]
print('Making list object eligible for GC... ')
# del l
time.sleep(10)
print('End of application.....')
time.sleep(10)
print('The End!!!!!....')
