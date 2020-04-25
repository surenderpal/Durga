from threading import *
import time
def display():
    for i in range(10):
        print('Lazy Daemon')
        time.sleep(2)
t=Thread(target=display)
t.setDaemon(True)
t.start()
time.sleep(5)
print('End of main thread')
