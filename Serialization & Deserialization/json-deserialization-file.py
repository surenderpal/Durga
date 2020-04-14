import json
with open('emp.json','r') as f:
    display=json.load(f)
print(display)
print('*'*40)
print('Emp Name:',display['namee'])
print('Emp Age:',display['age'])
print('Salary',display['salary'])
print('Is Emp Married:',display['ismarried'])
print('Is Emp Haing GF:',display['isHavingGF'])
print('*'*40)
for k,v in display.items():
    print(k,':',v)
