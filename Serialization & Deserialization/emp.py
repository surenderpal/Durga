class employee:
    def __init__(self,eno,ename,esal,eaddr):
        self.eno=eno
        self.ename=ename
        self.esal=esal
        self.eaddr=eaddr
    def display(self):
        print("Eno:{}, Ename:{}, Esal:{}, Eaddr:{}".format(self.eno,self.ename,self.esal,self.eaddr))
# e=employee(101,'surender',10000,'Delhi')
# # e.display()
# os.system(sender.py)
