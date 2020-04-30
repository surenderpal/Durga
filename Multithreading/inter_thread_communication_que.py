from threading import *
import time
import random
import queue
q=queue.Queue()
def producer(q):
    while True:
        item=random.randint(1,100)
        print('Producer prodcing Item:',item)
        q.put(item)
        print('Producer giving notificaion')
        time.sleep(5)
def consumer(q):
    while True:
        print('Consumer waiting for the updation')
        print('Consumer consuming the Item',q.get())
        time.sleep(5)
t1=Thread(target=producer,args=(q,))
t2=Thread(target=consumer,args=(q,))
t1.start()
t2.start()
