from threading import *
l=RLock()
print('Main thread acquiring the Lock...')
l.acquire()
print('Main thread agian acquiring the Lock...')
l.acquire()
print('Main thread acquiring the Lock...')
