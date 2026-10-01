from abc import ABC, abstractmethod

class BankAccount(ABC):
        def __new__(cls, *args, **kwargs):
            if cls is BankAccount:
                raise TypeError("BankAccount abstrakt class, uni yaratib bo'lmaydi")
            return super().__new__(cls)

        def __init__(self, account_number, owner, balance):
            self._account_number = account_number
            self._owner = owner
            self._balance = balance

        @property
        def balance(self):
            return self._balance

        def deposit(self, amount):
            self._balance += amount

        def withdraw(self, amount):
            if amount > self._balance:
                print("mablag yeatarli emas")
            else:
                self._balance -= amount

        @abstractmethod
        def get_info(self):
            pass

        def __str__(self):
            return self.get_info()


        
        def __repr__(self):
            return f"{self.__class__.__name__}({self._account_number}, {self._owner}, {self._balance})"

        def __bool__(self):
            return self._balance > 0

        def __eq__(self, other):
            return self._balance == other._balance
    
        def __ne__(self, other):
            return self._balance != other._balance
    
        def __gt__(self, other):
            return self._balance > other._balance
    
        def __ge__(self, other):
            return self._balance >= other._balance
    
        def __lt__(self, other):
            return self._balance < other._balance
    
        def __le__(self, other):
            return self._balance <= other._balance

class SavingsAccount(BankAccount):
    def get_info(self):
        return f"jamgarma hisobi {self._owner}  {self._account_number}  Balans: {self._balance}"
 
 
class BusinessAccount(BankAccount):
    def get_info(self):
        return f"biznes hisobi | {self._owner}  {self._account_number}  Balans: {self._balance}"
 
 
account1 = SavingsAccount("UZ001", "Ali", 2500)
account2 = BusinessAccount("UZ2", "Vali", 6800)

print(account1)
print(repr(account1))
print(bool(account1))
 
print(account1 == account2)
print(account1 != account2)
 
print(account1 > account2)
print(account1 <= account2)

