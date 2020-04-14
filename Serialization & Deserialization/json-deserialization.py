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
{
    'name': 'surender', 
    'age': 30, 
    'salary': 1000, 
    'isMarried': True, 
    'IsHavingGF': None
}
