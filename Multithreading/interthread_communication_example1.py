from threading import *
import time
e=Event()
def consumer():
    print('Consumer Thread waiting for updation..')
    e.wait()
    print('Consumer Thread got notification and consuming the items...')
def producer():
    time.sleep(5)
    print('Producer thread producing items...')
    print('Producer thread giving notification by setting event')
    e.set()
t1=Thread(target=producer)
t2=Thread(target=consumer)
t1.start()
t2.start()

