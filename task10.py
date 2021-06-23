class Bank_Account: 
    def __init__(self): 
        self.balance=0
    def deposit(self): 
        amount=float(input("Enter amount to be Deposited: ")) 
        self.balance += amount 
        print("\n Amount Deposited:",amount) 
    def withdraw(self): 
        amount = float(input("Enter amount to be Withdrawn: ")) 
        if self.balance>=amount: 
            self.balance-=amount
            print("\n You Withdraw:", amount) 
        else: 
            print("\n Balance amount is less so you cannot withdraw ") 
    def display(self): 
        print("\n Net Available Balance=",self.balance) 
s=Bank_Account()
s.deposit()
s.withdraw()
s.display()
    
        
