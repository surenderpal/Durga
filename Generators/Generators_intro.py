# Nested colletions
# l=[x*x for x in range(10)]
# print(l)
# print('first element',l[0])
g=(x*x for x in range(1000000000))
# print(type(g))
while True:
    print(next(g))
