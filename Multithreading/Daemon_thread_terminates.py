from threading import *
import time
def display():
    for i in range(10):
        print('Lazy Daemon',i)
        time.sleep(2)
t=Thread(target=display) # t is non-daemon by nature
t.setDaemon(True) #we set the t explicitly as Daemon
t.start() 
time.sleep(5) #we stopped the non-daemon thread
print('End of main thread') #Daemon thread automatically stopped
