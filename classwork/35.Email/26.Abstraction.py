# Abstract class - no object
#2. Every child of abstract class -> 
from abc import ABC, abstractmethod

class BankAccount(ABC):
    def checkbalance(self, username):
        self.username = username
        print(f"\n\nHi {self.username}!!1\nDisplay the balance.")

    @abstractmethod
    def deposit(self):
        pass

    @abstractmethod
    def withdraw(self):
        pass
    
class CurrentAccount(BankAccount):
    def deposit(self):
        print("Any time deposit")

    def withdraw(self):
        print("No limits")

class SavingsAccount(BankAccount):
    def deposit(self):
        print("No limits for the deposit")

    def withdraw(self):
        print("Limits per day")

class SalaryAccount(BankAccount):
    def deposit(self):
        print("Deposit once in a month")

    def withdraw(self):
        print("No limit, Chargers are applied")
        
class JointAccount(BankAccount):
   def deposit(self):
        print("2 of them can deposit")
   def withdraw(self):
        print("No Limit, both can withdraw it")

class PensionAccount(BankAccount):
    def deposit(self):
        print("Once in a month")

    def withdraw(self):
        print("20K Per day")
        
class FixedDepositAccount(BankAccount):
    def deposit(self):
        print("One time Deposit")

    def withdraw(self):
        print("Once in a year")

saikrishna = CurrentAccount()
sanjeeva = SavingsAccount()
sumanth = SalaryAccount()
satishimran = JointAccount()
prasad = PensionAccount()
krishna = FixedDepositAccount()

saikrishna.checkbalance("Saikrishna")
saikrishna.deposit()
saikrishna.withdraw()

sanjeeva.checkbalance("Sanjeeva")
sanjeeva.deposit()
sanjeeva.withdraw()

sumanth.checkbalance("Sumanth")
sumanth.deposit()
sumanth.withdraw()

satishimran.checkbalance("Satish Imran")
satishimran.deposit()
satishimran.withdraw()

prasad.checkbalance("Prasad")
prasad.deposit()
prasad.withdraw()

krishna.checkbalance("Krishna")
krishna.deposit()
krishna.withdraw()
