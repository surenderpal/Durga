class customer:
    '''This class developed by surender and describes the bank operation'''
    bank_name='SBI'
    def __init__(self,name,balance=0.0):
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        self.balance=self.balance+amount
        print('After deposit your balance is',self.balance)
    def withdraw(self,amount):
        if self.balance<amount:
            print('Insufficient Funds....\nCant berform the operation!!')
        else:
            self.balance=self.balance-amount
            print('After withdraw balance is:',self.balance)
        
print('Welcome to',customer.bank_name,'bank')
name=input('Enter your name:')
c=customer(name)
while True:
    print('D-Deposit\nW-withdraw\nE-exit')
    option=input('Choose your option:')
    if option.lower()=='d':
        amount=float(input('Enter amount to deposit:'))
        c.deposit(amount)
    elif option.lower()=='w':
        amount=float(input('Enter amount to withdraw:'))
        c.withdraw(amount)
    elif option.lower()=='e':
        print('Thanks for Banking with us')
        break
    else:
        print('your option is Invalid, Pleae select valid option:')
        


