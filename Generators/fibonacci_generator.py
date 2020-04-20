#fibonacci series generator
def fibonacci_generator():
    a,b=0,1
    while True:
        yield a
        a,b= b,a+b
g=fibonacci_generator()    
for x in g:
    if x<=100:
        print(x)
    else:
        break
