#  Method overriding========================
# class Parent:
#     a=10
#     def properties(self):
#         print('Cash + Gold + Land + Power')
#         # print(self.a)
#     def marry(self):
    
#         print('Roopa')
# class Child(Parent):
#     def marry(self):
#         super().marry()
#         print('Antim')
#         self.a=20
#         print(self.a)
# c= Child()
# c.properties()
# c.marry()

# constructor overriding===================
class Parent:
    def __init__(self):
        print('Parent constructor')
class Child (Parent):
    # pass
    def __init__(self):     # constructor overrding 
        print('updated parent constructor')
        super().__init__()      #calling parent constructor

c=Child()
