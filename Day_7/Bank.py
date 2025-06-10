class BankAccount:
    OWNER_COUNT = 0
    TRANSACTIONS = 0
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self._balance = balance
        BankAccount.OWNER_COUNT += 1

    def owner(self):
        return self.owner

    def balance(self):
        return self._balance

    def deposit(self,amount):
        self._balance += amount    
        BankAccount.TRANSACTIONS += 1
    
    def withdraw(self,amount):
        if self._balance >= amount:
            self._balance -= amount
            BankAccount.TRANSACTIONS += 1
    def info(self):
        return f"Owner of Account: {self.owner}\nBalance:{self._balance}"
    
user1 = BankAccount("Kyle")
print(user1.balance())
user1.deposit(300)
print(user1.balance())
user1.withdraw(200)
print(user1.balance())

user2 = BankAccount("Anderson")
user2.deposit(500)

print(user1.info())
print(user2.info())


print(f"Our bank has {BankAccount.OWNER_COUNT} customer(s)")
print(f"Our bank has made {BankAccount.TRANSACTIONS} transaction(s) today")

