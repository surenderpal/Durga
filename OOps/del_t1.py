import time
class test:
    def __init__(self):
        print('Constructor created....')
    def __del__(self):
        print('Destructor created....')
t=test()
t = None
time.sleep(10)
print('End of program...')
print(t)
