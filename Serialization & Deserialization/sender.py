from emp import employee
import pickle
f=open('emp.ser','wb')
while True:
    eno=int(input('Enter Employee No:'))
    ename=input('Enter Employee Name:')
    esal=float(input('Enter Employee Salary:'))
    eaddr=input('Enter Employee address:')
    e=employee(eno,ename,esal,eaddr)
    pickle.dump(e,f)
    option=input('Do you want to serialize another object [Yes|No]')
    if option.lower()=='no':
        break 
print('mulitple object serialized..')
# f.close()
