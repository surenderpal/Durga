from threading import *
import time
s=Semaphore(5)
def wish(name):
    s.acquire()
    for i in range(10):
        print('Good Evening:',end='')
        time.sleep(2)
        print(name)
    s.release()
t1=Thread(target=wish,args=('Sachin',))
t2=Thread(target=wish,args=('Dhoni',))
t3=Thread(target=wish,args=('Yuvraj',))
t4=Thread(target=wish,args=('Kholi',))
t1.start()
t2.start()
t3.start()
t4.start()
