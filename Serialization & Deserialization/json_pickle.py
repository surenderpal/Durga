import jsonpickle
class Employee:
    def __init__(self,eno,ename,esal,eaddr,ismarried):
        self.eno=eno
        self.ename=ename
        self.esal=esal
        self.eaddr=eaddr
        self.ismarried=ismarried
    def display(self):
        print('Employee no is {},\nEmployee name is {},\nEmployee Salary is {}, \nEmployee Address is {},\nIs Employee Married {}'.format(self.eno,self.ename,self.esal,self.eaddr,self.ismarried))
e=Employee(100,'surender',1000.0,'Delhi',False)
# e.display()
#serailzing to json string
json_str=jsonpickle.encode(e)
print('encode',json_str)
#serializationto JSON File
with open('cust_emp.json','w') as f:
    f.write(json_str)
