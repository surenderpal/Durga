class Account:
    def __init__(self,initialbalance):
        self.__balance=initialbalance
    def getBalance(self):
        #Authentication or Validation
        return self.__balance
a=Account(10000)
# print(a.__balance)
print(a.getBalance())
