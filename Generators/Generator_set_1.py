# def mygen():
#     yield 'A'
#     yield 'B'
#     yield 'C'
# g=mygen()
# print(type(g))
# print(next(mygen()))
# print(next(g))
# print(next(g))
# for x in mygen():
# for x in g:
#     print(x)

def gen_first_n(n):
    i=1
    while i<=n:
        yield i
        i=i+1
g=gen_first_n(10) 
for x in g:
    print(x)
