# # # r=range(20)
# # # for x in r:
# # #     print x
# # # r=range(1,22,3)
# # # for x in r:
# # #     print(x)
# # # print(r[-1])
# # # print(r[0:4])
# # # print(r[2])
# # # r[1]=1000
# # # l=[1,2,3,4,5,5,6,7,7]
# # # b=bytes(l)
# # # print(type(b))
# # l=[10,29,30,40,255]
# # b=bytes(l)
# # print(type(b))
# # for x in b:
# #     print (x)
# # print(b[0])
# # b[0]=99
# l=[12,34,4,43]
# b=bytearray(l)
# print(type(b))
# print(b[0])
# b[2]=123
# for x in b:
#     print(x)
# print(b[-1])
# def f1():
#     return 10
# x=f1()
# # print(x)
# def f2():
#     print('hello')
# x=f2()
# print(x)
# a= None
# print(id(a))
# print(type(a))
a=None
b=None
c=None
def f1():
    pass
d=f1()
print(d)
print(id(d))
print(id(a))
print(id(b))
print(id(c))
