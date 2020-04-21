import random
import time
names=['surender','rahul','upika']
subject=['python','java','data science']
def student_list(num):
    students=[]
    for i in range(num):
        student={'Id':i,'Name':random.choice(names),'Subject':random.choice(subject)}
        students.append(student)
    return students
t1=time.perf_counter()
student_list(10000)
t2=time.perf_counter()
print('Time required to student list:',(t2-t1))



