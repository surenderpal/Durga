# # static method
# class bird:
#     wings=2
#     @classmethod
#     def fly(cls,name):
#         print('{} has {} wings'.format(name,cls.wings))
# bird.fly('bandya')
# bird.fly('parrot')
# ------doubt start------
# class test:
#     count=0
#     def __init__(self):
#         test.count=test.count+1
#     @classmethod
#     def getnoofobjects(cls):
#         print('the no of objects created',cls.count)
# test.getnoofobjects()
# t1=test()
# t2=test()
# t3=test()
# t4=test()
# test.getnoofobjects()
# ----------Static method------
# class surendermath:
#     @staticmethod
#     def add(a,b):
#         print('sum is',(a+b))
#     @staticmethod
#     def product(a,b):
#         print('Prodcut is',(a*b))
#     @staticmethod
#     def average(a,b):
#         print('Average is',(a+b)/2)
# surendermath.add(10,20)
# surendermath.product(10,20)
# surendermath.average(10,20)

# class test:
#     def m1(x):
#         print('some method')
# t=test()
# t.m1(13)
# # test.m1()
# ---Static Method-----
# class test:
#     def m1():
#         print('some method')
# test.m1()
# class test:
#     def m1(x):
#         print('Some method')
# test.m1(10)


# Accessing member of one class inside another class
class employee:
    def __init__(self,eno,ename,esal):
        self.eno=eno
        self.ename=ename
        self.esal=esal
    def display(self):
        print('Employee number is',self.eno)
        print('Employee name is',self.ename)
        print('Employee Salary is',self.esal)
emp=employee(101,'surender',45000)
class manager:
    def updateEmpSal(emp):
        emp.esal=emp.esal+10000
        emp.display() 

manager.updateEmpSal(emp)

