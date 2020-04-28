from threading import *

def consumer(c):
    c.acquire()
    print('consumer waiting for updation.')
    c.wait() #now thread will entered into the waiting state
    print('consumer got notification & consuming the item')
    c.release()    
def producer(c):
    c.acquire()
    print('Producer producing item')
    print('Producer giving the notification')
    c.notify()
    c.release()
c=Condition()
t1=Thread(target=consumer,args=(c,))
t2=Thread(target=producer,args=(c,))
t1.start()
t2.start()
