#1. Check if three lengths form an Equilateral, Isosceles, or Scalene triangle
a, b, c = tuple(map(int, input().split()))

if a == b and a==c and b == c:
                print("Equ")
elif a != b and b != c and a != c:
    print("Sca")
else:
    print("Iso")

#2. Classify a character as: vowel, consonant, digit, special character
ch = input()

vol = 'aeiouAEIOU'

if ch in vol:
    print("Vol")
elif ch.isalpha():
    print("Con")
elif ch.isdigit():
    print("Dig")
else:
    print("Special")

#3. BMI Calculator and Category

height = float(input())
weight = float(input())
bmi = weight / (height ** 2)

if bmi < 18.5:
    print("Underweight")
elif 18.5 <= bmi < 25:
    print("Normal")
elif 25 <= bmi < 30:
    print("Overweight")
else:
    print("Obese")
print(bmi)

#4. Electricity bill calculator based on units used

units = int(input())
charge = 0

if units <= 100:
    charge = units * 1
elif 100 < units <= 200:
    charge = 100 + (units - 100) * 2
else:
    charge = 300 + (units - 200) * 3

print(charge)

#5. Check if a number is Armstrong

num = input()
res = 0
l = len(num)

for i in num:
    res += int(i) ** l

if res == int(num):
    print("Arm")
else:
    print("Not Arm")
    
print(res)

#6. Validate strong password (min 8 chars, 1 uppercase, 1 digit, 1 specialchar)

password = input("Enter password: ")

if len(password) >= 8:
    if any(ch.isupper() for ch in password):
        if any(ch.isdigit() for ch in password):
            if any(ch in "!@#$%^&*()-_=+[]{};:'\",.<>?/|" for ch in password):
                print("Strong Password")
            else:
                print("Weak Password")
        else:
            print("Weak Password")
    else:
        print("Weak Password")
else:
    print("Weak Password")

#7. ATM Withdrawal Simulation

balance = int(input())
withdrawal = int(input())
if withdrawal >= 500 and withdrawal % 100 == 0 and withdrawal <= balance:
    balance -= withdrawal
    print("Success")
    print(balance)
else:
    print("Insufficient Balance")

#8. Ticket fare calculator with age-based discounts

age = int(input())
price = 200
fare = 0

if age < 5:
    fare = 0
elif 5 <= age <= 18:
    fare = 100 - 100 * 0.5
elif age > 60:
    fare = price - price * 0.3
else:
    fare = price

print(fare)

#9. 24-hour to 12-hour time converter

time = input()
hours, minutes = map(int, time.split(":"))
period = "AM"
if hours == 0:
    hours = 12
elif hours == 12:
    period = "PM"
elif hours > 12:
    hours -= 12
    period = "PM"
print(f"{hours}:{minutes:02d} {period}")

#10. Find category of a character based on ASCII range

char = input()
ascii_value = ord(char)
if 65 <= ascii_value <= 90 or 97 <= ascii_value <= 122:
    print("Alphabet")
elif 48 <= ascii_value <= 57:
    print("Digit")
else:
    print("Special Symbol")

#11. Grading system with nested bands (including + and - grades)

score = int(input())
if 90 <= score <= 100:
    print("A")
elif 85 <= score <= 89:
    print("B+")
elif 80 <= score <= 84:
    print("B")
elif 70 <= score <= 79:
    print("C")
else:
    print("F")

#12. Currency denomination counter

amount = int(input())
denominations = [2000, 500, 100, 50, 20, 10, 5, 2, 1]
result = {}
for denom in denominations:
    count = amount // denom
    if count > 0:
        result[denom] = count
        amount -= count * denom
for denom, count in result.items():
    print(f"{count}x{denom}")

# 13. Movie ticket price based on day and age

day = input()
age = int(input())
if day in ["Saturday", "Sunday"]:
    price = 200
else:
    price = 150

if age < 12:
    price *= 0.5

print(f"${price}")

#14. Classify angle as Acute, Right, Obtuse, Straight

angle = int(input())
if angle < 90:
    print("Acute")
elif angle == 90:
    print("Right")
elif angle < 180:
    print("Obtuse")
elif angle == 180:
    print("Straight")

# 15. Grade college admission based on marks in 3 subjects

marks = list(map(int, input().split()))
average = sum(marks) / 3
if average > 90 and all(mark > 70 for mark in marks):
    print("Admit")
elif average >= 80:
    print("Waitlist")
else:
    print("Reject")

#16. Check if a number is perfect

num = int(input())
divisor_sum = sum(i for i in range(1, num) if num % i == 0)
if divisor_sum == num:
    print("Perfect")
else:
    print("Not Perfect")

# 17. Identify type of triangle by angles

angles = list(map(int, input().split()))
if all(angle < 90 for angle in angles):
    print("Acute")
elif any(angle == 90 for angle in angles):
    print("Right")
else:
    print("Obtuse")

#18. Convert marks (0–100) to 10-point GPA scale

marks = int(input())
if 91 <= marks <= 100:
    gpa = 10
elif 81 <= marks <= 90:
    gpa = 9
elif 71 <= marks <= 80:
    gpa = 8
elif 61 <= marks <= 70:
    gpa = 7
elif 51 <= marks <= 60:
    gpa = 6
elif 41 <= marks <= 50:
    gpa = 5
else:
    gpa = 4
print(gpa)

#19. Check if four digits form a lucky number (sum of first two == last two)

number = input("Enter the number: ")
n = len(number)

if n % 2 == 0:
    l = list(map(int, number))
    if (sum(l[:n//2]) == sum(l[n//2:])):
        print("lucky number")
    else:
        print("Unlucky number")
else:
    print("Unlucky number")

#20. Car insurance premium based on age and experience

age = int(input())
experience = int(input())
if age < 25 and experience < 3:
    print("High Risk")
elif age > 25 and experience > 5:
    print("Low Risk")
else:
    print("Medium Risk")

#21. Ticket system for amusement park

age = int(input())
if age < 12:
    fare = 50
elif age < 60:
    fare = 100
else:
    fare = 60

print(f"${fare}")

#22. Classify number as Single, Double, or Triple digit

num = int(input())
if 0 <= num <= 9:
    print("Single Digit")
elif 10 <= num <= 99:
    print("Double Digit")
else:
    print("Triple Digit")

#23. Validate time input (HH:MM format)

hrs, mins = tuple(map(int, input("Enter the time (HH:MM): ").split(':')))

if 0 <= hrs < 24 and 0 <= mins < 60:
    print("Valid Time")
else:
    print("Invalid time")

#24. Weather categorization by temperature

temp = int(input())
if temp < 10:
    print("Very Cold")
elif 10 <= temp <= 20:
    print("Cold")
elif 21 <= temp <= 30:
    print("Warm")
else:
    print("Hot")

#25. Assign mobile plan based on usage

usage = float(input("Enter data usage in GB: "))
if usage < 1:
    plan = "Plan A"
elif usage < 5:
    plan = "Plan B"
else:
    plan = "Plan C"

print(plan)

#26. Identify duplicate digits in a 3-digit number

num=input()
if len(set(num))==len(num):
    print("unique")
else:
    print("duplicates")
print(len(num)-len(set(num)))

# 27. Weekday classifier (Input: 1–7, Output: Day type)

data={
    1:"mon - wd",
    2:"Tue - wd",
    3:"wed - wd",
    4:"Thur - wd",
    5:"fri - wd",
    6:"sat - we",
    7:"sun - we",
    }
num=int(input())
print(data[num])

#28. Student attendance eligibility (> 75% to write exam)

attended=int(input("classes attended: "))
total=int(input("total classes: "))
percentage=(attended/total)*100
if percentage>75:
    print("eligible")
else:
    print("not eligible")

#29. Print grade trend based on increasing or decreasing scores

scores = list(map(int, input().split()))
if scores == sorted(scores):
    print("Improving")
elif scores == sorted(scores, reverse=True):
    print("Declining")
else:
    print("Fluctuating")

#30. Validate mobile number (10 digits, starts with 6–9)

num = input("Enter the mobile number: ")

if len(num) == 10:
    if num.isdigit():
        sts = '6789'
        if num[0] in sts:
            print("Valid Number")
        else:
            print("Number needs to starts with 6 - 9")
    else:
        print("Enter the digits properly [0 - 9]")

else:
    print("Length needs to 10")
