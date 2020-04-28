# In Bounded semaphore no of release call can't exceeds the acquire call
from threading import *
s=BoundedSemaphore(2)
s.acquire()
s.acquire()
s.release()
s.release()
s.release()
s.release()
s.release()
s.release()
s.release()
print('Releasing lock more times then acquire')
