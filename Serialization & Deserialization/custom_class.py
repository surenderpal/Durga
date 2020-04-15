import json
class Employee:
    def __init__(self,eno,ename,esal,eaddr):
        self.eno=eno
        self.ename=ename
        self.esal=esal
        self.eaddr=eaddr
    def display(self):
        print('Employee No is {}, Employee Name is {}, Employee Salarys is {} and Employee Address is{}'.format(self.eno,self.ename,self.esal,self.eaddr))
e=Employee(100,'surender',1000,'Delhi')
e.display()
