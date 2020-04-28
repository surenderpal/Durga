from threading import *
import time
e=Event()
# def drivers():
#     print('Drivers are waiting for the Green signal to drive their vehicle...')
#     e.wait()
#     print('Now Drivers are driving their vehicle')
# def TrafficPolice():
#     time.sleep(5)
#     print('Traffic Police producing the green signal')
#     e.set()
#     print('Traffic Police set the signal to green')
# t1=Thread(target=TrafficPolice)
# t2=Thread(target=drivers)
# t1.start()
# t2.start()
def TrafficPolice():
    while True:
        time.sleep(20)
        print('Traffic police given GREEN signal')
        e.set()
        time.sleep(20)
        print('Traffic police given RED signal')
        e.clear()
def driver():
    num=0
    while True:
        print('Drivers waiting for Green signal')
        e.wait()
        print('Traffic signal is GREEN.. Vehicels can move..')
        while e.isSet():
            num=num+1
            print('Vehilce Number:',num,'Crossing the signal')
            time.sleep(1)
        print('Traffic signal is RED...,Drivers have to wait')
t1=Thread(target=TrafficPolice)
t2=Thread(target=driver)
t1.start()
t2.start()
