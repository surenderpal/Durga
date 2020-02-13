# l1=[(1,2,3,4),(5,6,7,8)]
# print(l1[0][1])
# print(l1[1][2])
d={
    'cars':('Innova','Honda','Maruti'),
    'mobiles':('Samsung','iPhone','Nokia')
}
# print(d['cars'][1])
# print(d['mobiles'][1])
# print(d.get('cars')[2])
print(d['mobiles'])
# print(d.get('mobiles'))
# for x in d['mobiles']:
for x in d.get('mobiles'):
    print(x)
