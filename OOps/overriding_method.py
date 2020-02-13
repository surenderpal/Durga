class Person:
    def __init__(self,name,age,height,weight):
        self.name=name
        self.age=age
        self.height=height
        self.weight=weight
    def display(self):
        print('Name: ',self.name)
        print('Age: ',self.age)
        print('Height: ',self.height)
        print('Weight: ',self.weight)
class Employee(Person):
    def __init__(self,name,age,height,weight,eno,esal):
        # self.name=name
        # self.age=age
        # self.height=height
        # self.weight=weight
        super().__init__(name,age,height,weight)
        self.eno=eno
        self.esal=esal
    def display(self):
        # print('Name: ',self.name)
        # print('Age: ',self.age)
        # print('Height: ',self.height)
        # print('Weight: ',self.weight)
        super().display()
        print('Eno: ',self.eno)
        print('Esal: ',self.esal)
e=Employee('Surender',28,5.5,70,78,10000)
e.display()
