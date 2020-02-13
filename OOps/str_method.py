class Student:
    def __init__(self,name,rollno,marks):
        self.name=name
        self.rollno=rollno
        self.marks=marks
    def __str__(self):
        # return self.name
        return "Name:{},Roll no:{} and Marks:{}".format(self.name,self.rollno,self.marks)
s1=Student('surender',78,100)
s2=Student('rahul',79,200)
print(s1)
print(s2)
