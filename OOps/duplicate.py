# --------------------------------------------------------------
# dulicate elements in list for integers and string
l=[1,2,3,4,5,6,7,78,89,1,2,3,4,5]
# l=['surender','hello','rahul','rahul','surende']
s=set()
print('Name\Char\t\tCount')
for x in l:
    if x not in s:
        s.add(x)
        print('{}\t{}'.format(x,l.count(x)))
        # print(x,''.ljust('10',''),l.count(x))
