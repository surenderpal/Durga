import pickle
class employee:
    def __init__(self,eno,ename,esal,eaddr):
        self.eno=eno
        self.ename=ename
        self.esal=esal
        self.eaddr=eaddr
    def display(self):
        print("Emp NO: {}, Emp Name: {}, Emp Salary:{}, Emp Adderess:{}".format(self.eno,self.ename,self.esal,self.eaddr))

e=employee(100,'surender',10000,'Delhi')
e=employee(101,'rahul',1000,'Dwarka')
with open('emp.ser','wb') as f:
    pickle.dump(e,f)

with open('emp.ser','rb') as f:
    new_obj=pickle.load(f)
new_obj.display()
