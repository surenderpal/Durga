from threading import *
import time
l=Lock()
def wish(name):
    l.acquire()
    for i in range(10):
        print('Good Morning:',end='')
        time.sleep(2)
        print(name,i)
    # l.release()
t1=Thread(target=wish,args=('Surender',))
t2=Thread(target=wish,args=('rahul',))
t3=Thread(target=wish,args=('Upika',))
t4=Thread(target=wish,args=('Roopa',))
t1.start()
t2.start()
t3.start()
t4.start()
time.sleep(25)
print('Main thread wont reaquire lock...')
print("Is T1 alive:",t1.name,t1.is_alive())
