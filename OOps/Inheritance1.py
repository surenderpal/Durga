class p:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def eatndrink(self):
        print('Eat Biryani and drink Beer...')
class emp(p):
    def __init__(self,name,age,eno,esal):
        # self.name=name
        # self.age=age
        super().__init__(name,age)
        self.eno=eno
        self.esal=esal
    def work(self):
        print('Coding python3 program...')
    def empInfo(self):
        print('Name',self.name)
        print('Age',self.age)
        print('E_No',self.eno)
        print('E_sal',self.esal)
e=emp('surender',29,61355831,10000000)
e.eatndrink()
e.work()
e.empInfo()
  