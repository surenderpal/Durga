import time
numbers=[1,2,3,4,5,6]
def doubles(numbers):
    for  i in numbers:
        time.sleep(1)
        print('Double of ',i,':',2*i) 
def squares(numbers):
    for i in numbers:
        time.sleep(1)
        print('Square of ',i,':',i*i) 
begintime=time.time()
doubles(numbers)
squares(numbers)
endtime=time.time()
print('Total time taken:',endtime - begintime)
