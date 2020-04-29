# In semaphore no of release call can exceeds the acquire call
from threading import *
s=Semaphore(3)
# s=BoundedSemaphore(2)
s .acquire()
print('Main thread trying to acquire lock...')
s.acquire()
print('Main thread trying to acquire lock second time....')
s.acquire()
print('Main thread trying to acquire lock third time...')
s.release()
s.release()
s.release()
s.release()
