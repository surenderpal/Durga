import queue
q=queue.LifoQueue()
q.put(1)
q.put(2)
q.put(3)
q.put(4)
while not q.empty():
    print(q.get(),end= ' ')
