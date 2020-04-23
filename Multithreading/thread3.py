from threading import *
def display():
    for i in range(10):
        print('Child Thread')
t=Thread(target=display) #Main thread creates child thread object
t.start() #Main thread starts child thread object
for i in range(10):
    print('Main thread')
