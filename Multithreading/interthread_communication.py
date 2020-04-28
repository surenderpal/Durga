#====================Inter thread communication============
Producer-consumer:
1-Event
2-Condition
3-Queue
#==========================================================
# InterThread communication by using Event:
Event :-
Signal and wait
e=Event()
method of Event class 
1. set()
e.set()
2. clear()
e.clear()
3. wait() or wait(time)==Thread can waith until event is set


1) set()  internal flag value will become True and it represents GREEN signal for all waiting threads. 
2) clear()  inernal flag value will become False and it represents RED signal for all waiting threads. 
3) isSet()  This method can be used whether the event is set or not 
4) wait()|wait(seconds)  Thread can wait until event is set
