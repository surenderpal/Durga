class Person:
    def __init__(self,name,age,height,weight):
        self.name=name
        self.age=age
        self.height=height
        self.weight=weight
    def display(self):
        print('Name:',self.name)
        print('Age:',self.age)
        print('Height:',self.height)
        print('Weight:',self.weight)
class Student(Person):
    def __init__(self,name,age,height,weight,rollno,marks):
        # self.name=name
        super().__init__(name,age,height,weight)
        # self.age=age
        # self.height=height
        # self.weight=weight
        self.rollno=rollno
        self.marks=marks
    def display(self):
        super().display()
        # print('Name:',self.name)
        # print('Age:',self.age)
        # print('Height:',self.height)
        # print('Weight:',self.weight)
        print('Roll No:',self.rollno)
        print('Marks:',self.marks)
# p=Person('surender',29,165,66)     
s=Student('surender',29,165,66,78,100)
s.display()
