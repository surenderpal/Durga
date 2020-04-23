from threading import *
import time
def doubles(numbers):
    for  i in numbers:
        time.sleep(1)
        print('Double:',2*i) 
def squares(numbers):
    for i in numbers:
        time.sleep(1)
        print('Square:',i*i)
numbers=[1,2,3,4,5,6] 
begintime=time.time()
t1=Thread(target=doubles,args=(numbers,))
t2=Thread(target=squares,args=(numbers,))
t1.start()
t2.start()
t1.join()
t2.join()
endtime=time.time()
print('Total time taken:',endtime-begintime)
