class Account:
    def __init__(self,initial_balance):
        self.__balance=initial_balance
    def getBalance(self):
        #Authentication/Validation
        return self.__balance
    def Deposit(self,amount):
        #Authentication/Validation
        self.__balance=self.__balance+amount
    def Withdraw(self,amount):
        #Authentication/Validation
        self.__balance=self.__balance-amount
a=Account(100000)
print('Balance in your account:',a.getBalance())
a.Withdraw(1000)
print('after withdrawing your balance is: ',a.getBalance())
a.Deposit(200000)
print('after depositing your balance is: ',a.getBalance())
