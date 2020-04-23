from threading import *
class test:
    def display(self):
        for i in range(10):
            print('Child Thread executing Name:',current_thread().getName())
o=test()
# t=Thread(target=test().display) 
t1=Thread(target=o.display)
t2=Thread(target=o.display)
t3=Thread(target=o.display)
t4=Thread(target=o.display)
t1.start()
t2.start()
t3.start()
t4.start()
# for i in range(10):
#     print('Main Thread Executing Name: ',current_thread().getName())
