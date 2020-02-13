from abc import *
class CollegeAutomation(ABC):
    @abstractmethod
    def m1(self):pass
    @abstractmethod
    def m1(self):pass
    @abstractmethod
    def m1(self):pass
class abs(CollegeAutomation):
    def m1(self):
        print('M1 method implementation')
    def m2(self):
        print('M2 method implementation')
class concrete(abs):
    def m3(self):
        print('M3 method implementation')
c=concrete()
c.m1()
c.m2()
c.m3()
