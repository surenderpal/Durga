import queue
q=queue.PriorityQueue()
# q.put(1)
# q.put(3)
# q.put(5)
# q.put(4)
# q.put(2)
# q.put(0)

# alphabatical priority
q.put((1,'Ram Lakhan'))
q.put((3,'Rahul'))
q.put((5,'Roopa'))
q.put((2,'Mithlesh'))
q.put((4,'Upika'))
q.put((6,'Surender'))
while not q.empty():
    # print(q.get(),end=' ')
    print(q.get()[1],end=' ')# hiding indexes
