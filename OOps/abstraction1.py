# class test:       #concate(normal) class
#     pass
# t=test()

# # abstract class with no abstract method is eligible for instantiation
# from abc import *
# class test(ABC):
#     pass
# t=test()

# # abstract class with one abstract method is eligible for instantiation
# from abc import *
# class test(ABC):
#     pass
#     @abstractmethod
#     def m1(self):
#         pass
# t=test()

# # normal class with one abstract method.
# from abc import *
# class test:
#     @abstractmethod
#     def m1(self):
#         pass
# t=test()
 
# abstract class with method m1 and without implementation of m1 in subclass
# from abc import *
# class test(ABC):
#     @abstractmethod
#     def m1(self):
#         pass
# class subtest(test):
#     pass
# s=subtest()
# s.m1()

# abstract class with method m1 and m2 and without implementation of method m2 in child class

# from abc import *
# class test(ABC):
#     @abstractmethod
#     def m1(self):
#         pass
#     @abstractmethod
#     def m2(self):
#         pass
# class subclass(test):
#     def m1(self):
#         print('m1 method')
# s=subclass()
# s.m1()

# abstract class with method m1 and m2 and with implementation of both method m1 and m2

# from abc import *
# class test(ABC):
#     @abstractmethod
#     def m1(self):
#         pass
#     @abstractmethod
#     def m2(self):
#         pass

# class subclass(test):
#     def m1(self):
#         print('m1 method')
#     def m2(self):
#         print('m2 method')
# s=subclass()
# s.m1()
# s.m2()

# abstract class with method m1 and m2(abstract method) and with implementation of m2 method
from abc import *
class test(ABC):
    def m1(self):
        pass
    @abstractmethod
    def m2(self):
        pass
class subclass(test):
    def m2(self):
        print('M2 method')
s=subclass()
s.m2()
