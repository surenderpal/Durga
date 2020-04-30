from threading import *
import queue
q=queue.Queue()
q.put(4)
q.put(5)
q.put(6)
q.put(7)
while not q.empty():
    print(q.get())
