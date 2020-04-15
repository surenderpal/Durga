import json
class Employee:
    def __init__(self,eno,ename,esal,eaddr):
        self.eno=eno
        self.ename=ename
        self.esal=esal
        self.eaddr=eaddr
    def display(self):
        print('Employee No is {}, \nEmployee Name is {}, \nEmployee Salarys is {} and \nEmployee Address is {}'.format(self.eno,self.ename,self.esal,self.eaddr))
e=Employee(100,'surender',1000,'Delhi')
e_dict={'eno':e.eno,'ename':e.ename,'esal':e.esal,'eaddr':e.eaddr}
print('converted custom class to Dict:',e_dict)
