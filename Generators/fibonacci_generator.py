#fibonacci series generator
def fibonacci_generator():
    a,b=0,1
    while True:
        yield a
        a,b= b,a+b
g=fibonacci_generator()    
# for x in g:
#     if x<=100:
#         print(x)
#     else:
#         break

#first N fibonacci numbers
count=1
n=int(input('Enter number of fibonacci numbers Required:'))
while count<=n:
    print(next(g))
    count=count+1
