import time
class test:
    def __init__(self):
        print('Object creation is complete...')
    def __del__(self):
        print('Fulfulling the last wish and performing the clean up activity....')
t=test()
t1=test()
# t= None     
time.sleep(10)
print('End of Applicaion....')
