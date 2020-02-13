from abc import *
class CollegeAutomation(ABC):
    @abstractmethod
    def m1(self):
        pass
    @abstractmethod
    def m2(self):
        pass
    @abstractmethod
    def m3(self):
        pass
class SurenderSoftwareSolutions(CollegeAutomation):
    def m1(self):
        print('M1 method implementation')
    def m2(self):
        print('M2 method implementation')
    def m3(self):  
        print('M3 method implementation')
sp=SurenderSoftwareSolutions()
sp.m1()
sp.m2()
sp.m3()
