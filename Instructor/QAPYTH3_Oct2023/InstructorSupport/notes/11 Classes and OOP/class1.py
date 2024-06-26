from Account import Account

some_account = Account(1000.00) 
some_account.deposit(550.23)
some_account.deposit(100) 
some_account.withdraw(50) 
print(some_account.getbalance()) 

another = Account(0)
print(Account.numCreated)
print("object another is class",
       another.__class__.__name__) 


