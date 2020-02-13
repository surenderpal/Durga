# Abstract method

# from abc import abstractmethod
# class Vehicle:
#     @abstractmethod
#     def getNoOfWheels(self):
#         pass
# v=Vehicle()
  
# Abstract class 
from abc import abstractmethod,ABC
class Vehicle(ABC):
    @abstractmethod
    def getNoOfWheels(self):
        pass
class Bus(Vehicle):
    def getNoOfWheels(self):
        return 4
class Auto(Vehicle):
    def getNoOfWheels(self):
        return 3
b=Bus() 
print(b.getNoOfWheels())
a=Auto()
print(a.getNoOfWheels())
