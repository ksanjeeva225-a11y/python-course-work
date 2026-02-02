'''Q1. Polymorphism – Employee Salary (Method
Overriding)
Create a base class Employee with a method calculate_salary().
Create a derived class Manager that overrides the method.
● Employee salary = basic salary
● Manager salary = basic salary + bonus
Input:
Enter basic salary: 30000
Enter bonus: 5000

Expected Output:
Final Salary: 35000
'''
class Employee:
    def calculate_salary(self, basic):
        return basic

class Manager(Employee):
    def calculate_salary(self, basic, bonus):
        return basic + bonus

basic_salary = int(input("Enter basic salary: "))
bonus = int(input("Enter bonus: "))

m = Manager()
final_salary = m.calculate_salary(basic_salary, bonus)

print("Final Salary:", final_salary)
'''
Q2. Polymorphism – Bank Interest Calculation
Create a base class Bank with a method get_interest_rate().
Create a derived class SavingsAccount that overrides the method to provide higher
interest.
Input:
Enter principal: 10000
Enter time (years): 2

Expected Output:
Interest Amount: 1200
'''
class Bank:
    def get_interest_rate(self):
        return 0.05

class SavingsAccount(Bank):
    def get_interest_rate(self):
        return 0.06

principal = int(input("Enter principal: "))
time = int(input("Enter time (years): "))

account = SavingsAccount()
interest = principal * account.get_interest_rate() * time

print("Interest Amount:", int(interest))
'''
Q3. Operator Overloading – Distance Addition
Create a class Distance with attributes meters and centimeters.
Overload the + operator to add two distance objects.
Input:
Distance 1: 2 meters 50 centimeters
Distance 2: 1 meter 75 centimeters

Expected Output:
Total Distance: 4 meters 25 centimeters
'''
class Distance:
    def __init__(self, meters, centimeters):
        self.meters = meters
        self.centimeters = centimeters

    def __add__(self, other):
        total_cm = self.centimeters + other.centimeters
        total_m = self.meters + other.meters + total_cm // 100
        total_cm = total_cm % 100
        return Distance(total_m, total_cm)

d1 = Distance(2, 50)
d2 = Distance(1, 75)

d3 = d1 + d2

print("Total Distance:", d3.meters, "meters", d3.centimeters, "centimeters")
'''
Q4. Abstraction – Vehicle Fuel Type
Create an abstract class Vehicle with an abstract method fuel_type().
Create subclasses Car and Bike and implement the method.
Input:
No input

Expected Output:
Car Fuel Type: Petrol
Bike Fuel Type: Petrol
'''
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def fuel_type(self):
        pass

class Car(Vehicle):
    def fuel_type(self):
        return "Petrol"

class Bike(Vehicle):
    def fuel_type(self):
        return "Petrol"

car = Car()
bike = Bike()

print("Car Fuel Type:", car.fuel_type())
print("Bike Fuel Type:", bike.fuel_type())
'''
Q5. Abstraction – Payment System
Create an abstract class Payment with an abstract method pay_amount().
Create subclasses CreditCardPayment and UPIPayment.
Input:
Enter amount: 2000

Expected Output:
Payment of 2000 successful using Credit Card
Payment of 2000 successful using UPI
'''
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay_amount(self, amount):
        pass

class CreditCardPayment(Payment):
    def pay_amount(self, amount):
        print(f"Payment of {amount} successful using Credit Card")

class UPIPayment(Payment):
    def pay_amount(self, amount):
        print(f"Payment of {amount} successful using UPI")

amount = int(input("Enter amount: "))

cc = CreditCardPayment()
upi = UPIPayment()

cc.pay_amount(amount)
'''
Q6. Exception Handling – Division Calculator
Write a program to divide two numbers using exception handling.
Handle ZeroDivisionError and ValueError.
Input:
Enter numerator: 10
Enter denominator: 0

Expected Output:
Cannot divide by zero!
'''
try:
    num = int(input("Enter numerator: "))
    den = int(input("Enter denominator: "))
    result = num / den
    print("Result:", result)
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Invalid input")
'''
Q7. Exception Handling – ATM Withdrawal
Simulate ATM withdrawal with exception handling.
Handle:
● Insufficient balance
● Invalid withdrawal amount
Input:
Enter balance: 5000
Enter withdrawal amount: 7000

Expected Output:
Insufficient balance
'''

try:
    balance = int(input("Enter balance: "))
    withdraw = int(input("Enter withdrawal amount: "))

    if withdraw <= 0:
        raise ValueError("Invalid withdrawal amount")
    if withdraw > balance:
        raise Exception("Insufficient balance")

    balance -= withdraw
    print("Withdrawal successful")
except ValueError:
    print("Invalid withdrawal amount")
except Exception as e:
    print(e)
'''
Q8. Exception Handling – Age Validation
Accept user age and raise exception if age is invalid.
Input:
Enter age: 3

Expected Output:
Invalid age
'''
try:
    age = int(input("Enter age: "))
    if age < 5:
        raise Exception("Invalid age")
    print("Valid age")
except:
    print("Invalid age")
'''
Q9. File Operations – Write Student Data
Write a program to store student name and marks in a file named students.txt.
Input:
Enter name: Arun
Enter marks: 85

Expected Output:
Data saved successfully
'''
name = input("Enter name: ")
marks = input("Enter marks: ")

file = open("students.txt", "w")
file.write(f"Name: {name}, Marks: {marks}")
file.close()
'''
Q10. File Operations – Read Student Data
Read and display the contents of students.txt.
Input:
No input

Expected Output:
Name: Arun, Marks: 85
'''
file = open("students.txt", "r")
data = file.read()
file.close()

print(data)
