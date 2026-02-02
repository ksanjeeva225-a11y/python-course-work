#Q1. Automated Salary Tax Calculator
sal = int(input("Enter the sal: "))
tax = 0

if sal <= 250000:
    tax = 0
elif 250000 < sal <= 500000:
    tax = sal * 0.05
elif 500000 < sal <= 1000000:
    tax = sal * 0.2
elif sal > 1000000:
    tax = sal * 0.3
print(f'Tax amount: {tax}\nSalary after tax: {sal-tax}')

#Q2. Movie Ticket Pricing System
n = int(input())
amount = 0
for i in range(n):
    age = int(input())
    if age <= 5:
        amount += 0
    elif 5 <= age <=18:
        amount += 100
    elif 19 <= age <= 60:
        amount += 150
    else:
        amount += 120
print(amount)

#3. Electricity Bill Generator
units = int(input("Enter the units: "))
price = 0
if units <= 100:
    price = units * 1.5
elif 100 < units <= 200:
    price = 150 + (units - 100) * 2.5
elif 200 < units <= 500:
    prive = 400 + (units - 200) * 4
elif units > 500:
    price = 1600 + (units -500) * 6

print(price)

#4. Car Parking Fee Calculator
hrs = int(input("Enter the hours: "))
fees = 0
if hrs <= 2:
    fees = 30
elif 2 < hrs < 24:
    fees = 30 + (hrs - 2) * 10
elif hrs == 24:
    fees = 200
print(fees)


#5.Product Inventory Checker (Nested Conditionals)
name = input("Enter the name: ")
qua = int(input("Enter the qua: "))
if qua == 0:
    print(f'{name}: Out of Stock')
elif 1 < qua <= 10:
    print(f'{name}: Low Stock')
elif 10 < qua <= 50:
    print(f'{name}: In Stock')
elif qua>50:
    print(f'{name}: Overstocked')

#6.Pattern – Row-wise Alternating 0 and 1 (Nested Loops)
n = int(input("Enter the size: "))
for i in range(n):
    for j in range(n):
        print((i + j) % 2, end = ' ')
    print()

#7.Gym Subscription Billing (Menu Driven Program)
billing = {1:500, 2:1300, 3:5000}
ch = int(input("Enter the choices: "))
n = int(input("No of people: "))
print(billing[ch] * n)

#8.Billing Bot – Apply Discount Based on Amount
amount = int(input("Enter the sal: "))
discount = 0

if 0 <= amount < 1000:
    discount = 0
elif 1000 <= amount < 5000:
    discount = amount * 0.05
elif 5000 <= amount < 10000:
    discount = amount * 0.1
elif amount > 10000:
    discount = amount * 0.15

print(amount - discount)

#9.ATM PIN Verification with Blocking Logic
str_pin = 1234
for i in range(3):
    pin = int(input("Enter the pin: "))
    if pin == str_pin:
        print("Access Granted")
        break
else:
    print("ATM Blocked. Try Again Later.")

#10.Bus Booking System – Track Full and Empty Seats
n = int(input("Enter the no of seats: "))
bs = tuple(map(int, input().split()))

print(f' Total Seats: {n}\nBooked: {len(bs)}\nAvailable : {n - len(bs)}')
