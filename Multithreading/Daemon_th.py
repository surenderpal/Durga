from threading import *
import time
print('Is Daemon:',current_thread().isDaemon())
print('Daemon:',current_thread().daemon)
#setting current thread to Daemon
# current_thread().setDaemon(True) #we are not allowed to change the nature of Main thread as it is already start with the start of programm
#we are not allowed to change the nature of child thread but only when thread is not started.
#By default Mian thread is Non-Daemon.
#for all remaiing thread daemon nature will be inherited from parent
def display():
    print('Child Thread:')
t=Thread(target=display)
t.setDaemon(True)
t.start()
print('Is Daemon Child thread:',t.isDaemon())
#The main purpose of Daemon thread is to provide support for non-daemon thread
#if last deamon thread terminates, then Daemon thread terminates automatially

