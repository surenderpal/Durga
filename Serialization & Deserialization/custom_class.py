import json
class Employee:
    def __init__(self,eno,ename,esal,eaddr):
        self.eno=eno
        self.ename=ename
        self.esal=esal
        self.eaddr=eaddr
    def display(self):
        print('Employee No is {}, \nEmployee Name is {}, \nEmployee Salarys is {} and \nEmployee Address is {}'.format(self.eno,self.ename,self.esal,self.eaddr))
e=Employee(100,'surender',1000,'Delhi')
# e_dict={'eno':e.eno,'ename':e.ename,'esal':e.esal,'eaddr':e.eaddr} #converting class to dict manually
e_dict=e.__dict__  #converting employee object to dict using .__dict__ function
# print('converted custom class to Dict:',e_dict)
# serializing to json string
# json_string=json.dumps(e_dict,indent=4,sort_keys=True)
# print(json_string)
# serializing dict object to json file
with open('custom.json','w') as f:
    json.dump(e_dict,f)
print('Custom Dict object dumped successfully!!!')
