class Car:
    def __init__(self,name,model,color):
        self.name=name
        self.model=model
        self.color=color
    def getinfo(self):
        print('Name:{},Model:{},Color:{}'.format(self.name,self.model,self.color))

class Employee:
    def __init__(self,ename,eno,car):
        self.ename=ename
        self.eno=eno
        self.car=car
    def empInfo(self):
        print('EmpName:{}'.format(self.ename))
        print('Eno:{}'.format(self.eno))
        print('Employee car info:')
        self.car.getinfo()
c=Car('Hond City','Top model 2020','White')
e=Employee('Surender','078',c)
e.empInfo()
