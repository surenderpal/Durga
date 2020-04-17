from pyaml import yaml
emp_dict={'name':'Surender',
            'age':20,
            'salary':1000.0,
            'IsMarried':True
        }
#serialization to yaml string
yaml_string=yaml.dump(emp_dict)
print(yaml_string)
# #serilaization to a yaml lfile
with open('emp.yaml','w') as f:
    yaml.dump(emp_dict,f)
#Deserialization from yamaml string
new_dict=yaml.safe_load(yaml_string)
print(new_dict)
for k,v in new_dict.items():
    print(k,':',v)
#Deserialization from yamaml file
with open('emp.yaml','r') as f:
    new_dict2=yaml.safe_load(f)
    print(new_dict2)
