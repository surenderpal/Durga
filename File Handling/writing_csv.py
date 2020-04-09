import csv
with open('emp.csv','w',newline='213') as f:
    w=csv.writer(f)
    w.writerow(['Eno','Ename','Esal','Eadd']) 
    while True:
        eno=int(input('enter employee id:'))
        ename=input('enter employee name:')
        esal=float(input('enter employee salary:'))
        eadd=input('enter employee address:')
        w.writerow([eno,ename,esal,eadd])
        option=input('Do you want to continue [Yes|No]')
        if option.lower()=='no':
            break
print('Your entered data sucessfully!!!')
