import json
employee={'namee':'surender','age':35,'salary':1000.0,'ismarried':True,'isHavingGF':None}
json_string=json.dumps(employee,indent=1,sort_keys=True) #serialize to string
print(json_string)
# {"namee": "surender", "age": 35, "salary": 1000.0, "ismarried": true, "isHavingGF": null}
