class Account: 
    numCreated = 0
    def __init__(self, initial): 
        self.balance = initial
        Account.numCreated += 1
    def deposit(self, amt): 
        self.balance = self.balance + amt 
    def withdraw(self,amt): 
        self.balance = self.balance - amt 
    def getbalance(self): 
        return self.balance 

