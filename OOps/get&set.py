class student:
    def setName(self,name):
        self.name=name
    def getName(self):
        return self.name
    def setMarks(self,marks):
        self.marks=marks
    def getMarks(self):
        return self.marks
n=int(input('Enter no of students:'))
students=[]
for x in range(n):
    # s=student()
    name=input('Enter student name:')
    marks=int(input('Enter marks:'))
    s=student()
    s.setName(name)
    s.setMarks(marks)
    students.append(s)
for g in students:
    print('Hello',g.getName())
    print('Your marks are:',s.getMarks())
    print()
