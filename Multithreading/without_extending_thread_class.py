from threading import *
class test:
    def display(self):
        for i in range(10):
            print('Child Thread-2')
o=test()
# t=Thread(target=test().display)
t=Thread(target=o.display)
t.start()
for i in range(10):
    print('Main Thread')
