from threading import *
def display():
    print('This code executed by child Thread:',current_thread().getName())
# display()
t=Thread(target=display) #MainThread creates child thread object
t.start() #Main thread starts ChildThread      
u=Thread(target=display)
u.start()
print('This code executed by Thread:',current_thread().getName())
  