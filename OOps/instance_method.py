class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self):
        print("Hi",self.name,"!!!")
        print('Your marks are:',self.marks)
    def grade(self):
        if self.marks >=60:
            print('you got First Grade')
        elif self.marks >=50:
            print('You got Second Grade')
        elif self.marks>=35:
            print('You got Third Grade')
        else:
            print('You failed, Go and study harder!!!')
n=int(input('Enter no of students:'))
for i in range(n):
    name=input('Enter student name:')
    marks=int(input('Enter student marks:'))
    s=student(name,marks)
    s.display()
    s.grade()
    print()

