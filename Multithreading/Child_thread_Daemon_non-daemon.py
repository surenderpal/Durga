from threading import *
import time
def job1():
    print('Job 1 Execution..')
    print(current_thread().name,'-Is Thread is Daemon:',current_thread().daemon)
    ct=Thread(target=job2,name='Child Thread 2')
    ct.setDaemon(False)
    print('Is Ct Daemon:',ct.daemon)
    ct.start()

def job2():
    print('job 2 execution..')
t=Thread(target=job1,name='Child Thread')
t.setDaemon(True)
t.start()
time.sleep(10)
