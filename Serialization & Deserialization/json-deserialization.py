import json
json_strint='''{
                "name":"surender",
                "age":30,
                "salary":1000,
                "isMarried": true,
                "IsHavingGF":null
            }'''
display=json.loads(json_strint)
print(type(display))
print(display)
print('Emp Name:',display['name'])
print('Emp Age:',display['age'])
print('Salary',display['salary'])
print('Is Emp Married:',display['isMarried'])
print('Is Emp Haing GF:',display['IsHavingGF'])

for k,v in display.items():
    print(k,':',v)
