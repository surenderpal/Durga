class Car:
    def __init__(self,name,model,color):
        self.name=name
        self.model=model
        self.color=color
    def getInfo(self):
        print('Car Name is {}\nModel is {} and \nColor is {}'.format(self.name,self.model,self.color))
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def eatndrink(self):
        print('Eat Biryani and drink Beer...')
class Employee(Person):
    def __init__(self,name,age,eno,esal,car):
        super().__init__(name,age)
        self.eno=eno
        self.esal=esal
        self.car=car
    def Work(self):
        print('Coding python3 for application....')
    def empInfo(self):
        print('Emp Name:',self.name)
        print('Emp Age:',self.age)
        print('Emp No:',self.eno)
        print('Emp Salary',self.esal)
        print('Emp Car Informations:')
        self.car.getInfo()
c=Car('Honda City','2020','Black')
# c.getInfo()
e=Employee('surender',29,78,10000000000,c) 
e.empInfo() 
e.Work()
e.eatndrink()
