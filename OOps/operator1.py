# class Book:
#     def __init__(self,pages):
#         self.pages=pages
#     def __add__(self,other):
#         total_pages=self.pages+other.pages
#         return total_pages

# b1=Book(100)
# b2=Book(200)
# print(b1+b2)
# b3=Book(500)
# print(b1+b3)
# print(b2+b3)

# =========magic method for > and <= =================

# class Student: 
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     # def __gt__(self,other):
#     def __le__(self,other):
#         return self.marks <= other.marks
# s1=Student('surender',100)
# s2=Student('Rahul',100)
# s3=Student('upika',50)
# print(s1<=s2)
# # print(s3>s2)

# =========magic method for *  ================= 
class Employee:
    def __init__(self,name,salaryperday):
        self.name=name
        self.salaryperday=salaryperday
    def __mul__(self,other):
        return self.salaryperday * other.workingday
class Timesheet:
    def __init__(self,name,workingday): 
        self.name=name
        self.workingday=workingday
    def __mul__(self,other):
        return self.workingday * other.salaryperday

e=Employee('roopa',500)
t=Timesheet('roopa',25) 
print('total wages',e*t)
print('total wages',t*e)
