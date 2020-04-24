from threading import *
import time
def display():
    for i in range(10):
        print('Seta Thread')
        time.sleep(2)
t=Thread(target=display)
t.start()
t.join(10)
for i in range(10):
    print('Modern Ram Thread')
