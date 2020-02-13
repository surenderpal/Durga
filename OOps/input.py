from sys import argv
args=argv[1:]
# b=str()
b=0
for x in args:
    a = eval(x)
    # print(type(a))
    b = b + a
print('Entered values sum is:',b)
