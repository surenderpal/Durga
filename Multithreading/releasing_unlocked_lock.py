from threading import *
l=Lock()
print('Main thread acquireing lock....')
# l.acquire() 
print('Main thread releaseing lock....')
l.release()
