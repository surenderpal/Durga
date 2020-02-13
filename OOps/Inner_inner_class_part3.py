class Person:
    def __init__(self,name,dd,mm,yyyy):
        print('Person object creation is complete....')
        self.name=name
        self.dob=self.Dob(dd,mm,yyyy)
    def info(self):
        print('Name is ',self.name)
        self.dob.display()
    class Dob:
        def __init__(self,dd,mm,yyyy):
            print('Dob object creation is complete.....')
            self.dd=dd
            self.mm=mm
            self.yyyy=yyyy
        def display(self):
            print('DOB={}/{}/{}'.format(self.dd,self.mm,self.yyyy))
p=Person('surender',24,2,1991)
p.info()
