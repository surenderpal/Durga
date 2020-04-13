from emp import employee
import pickle
f=open('emp.ser','rb')
print('Deserialize emp object & priting data:')
while True:
    try:
        e=pickle.load(f)
        e.display()
    except EOFError:
        break
print('all emp completed')
    # obj=pickle.load(f)
    # obj.display()
