def first_n_numbers(num):
    i=1
    while i<=num:
        yield i
        i=i+1
g=first_n_numbers(500000)
l=list(g)
print(l)
