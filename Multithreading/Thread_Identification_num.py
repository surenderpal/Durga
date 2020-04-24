from threading import *
import time
def test():
    print('Child Thread')
t=Thread(target=test)
t.start()
print('Main Thread Identification Number:',current_thread().ident)
print('Child Thread Identification Number:',t.ident)
print('Active Thread count',active_count())
 