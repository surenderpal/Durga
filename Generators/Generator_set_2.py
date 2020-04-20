# get count down generator
import time
def countdown_generator(n):
    while n>=1:
        yield n
        n=n-1
g=countdown_generator(10) 
for x in g:
    print(x) 
    time.sleep(1) 

