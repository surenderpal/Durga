# f=open('linux_basic_code.txt','r')
# print('Printing data from file',f.read())
# print()
# print('Reading only 20 characters',f.read(20))
# print()
# print('Reading only one line',f.readline())
# print()
# print('Reading all lines and printing it in list:',f.readlines())
# f.close()  


## how to read file line by line
# f=open('linux_basic_code.txt','r')
# l1=f.readline()
# l2=f.readline()
# print('line1:',l1,end='')
# print('line2:',l2,end='')
# f.close()

# # how to read file line by line using loop
# f=open('linux_basic_code.txt','r')
# count=1
# line=f.readline()
# while line!='':
#     print("line No:",count,line,end='')
#     line=f.readline()
#     count=count+1
# f.close()

# # how to readlines
# f=open('linux_basic_code.txt','r')
# count=1
# # l=f.readlines() 
# print(l)
# for line in l:
#     print('Line No:',count,line,end='')
#     count=count+1


## Using all read methods simultaneously
f=open('char.txt','r')
print(f.read(3))
print(f.read(3))
print(f.readline(),end='')
print(f.read(5))
# print(f.readlines())
print('reamaing data:')
print(f.read())
f.close()
