from threading import *
import time
def disply():
    print(current_thread().name,'started....')
    time.sleep(3)
    print(current_thread().name,'ended...')
print('The number of active threads:',active_count())
t1=Thread(target=disply,name='Child Thread 1')
t2=Thread(target=disply,name='Child Thread 2')
t3=Thread(target=disply,name='Child Thread 3')
t1.start()
t2.start()
t3.start()
l=enumerate()
for t in l:
    print('Name:',t.name)
    print('Thread Identification Number:',t.ident)
print('The number of active threads:',active_count())
time.sleep(4)
print('The number of active threads:',active_count())
l=enumerate()
for t in l:
    print('Name:',t.name)
