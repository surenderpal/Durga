from threading import *
import time
def wish(name):
    for i in range(10):
        print('Good Evening:',end='')
        time.sleep(2)
        print(name)
t=Thread(target=wish,args=('surender',))
t2=Thread(target=wish,args=('rahul',))
t.start()
t2.start()
