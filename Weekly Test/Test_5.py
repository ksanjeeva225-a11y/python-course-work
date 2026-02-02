#1. Compute Geometric Values (Math Module)
import math

def circle_geometry(r):
    t = (round(math.pi * r * r, 2), round(2 * math.pi * r, 2))
    return t

print(circle_geometry(7))
print(circle_geometry(2.5))
#OR
import math

circle_geometry = lambda r: (round(math.pi * r * r, 2), round(2 * math.pi * r, 2))

print(circle_geometry(7))
print(circle_geometry(2.5))

#2. Random Team Picker (Random Module)
import random
def pick_random_team(members, team_size):
    print(random.choices(members, k = team_size))

pick_random_team(["Alice", "Bob", "Charlie", "David"],2)
pick_random_team(["A", "B", "C", "D", "E"],3)

#3. Temperature Alert (Lambda + Filter)
temp = [36, 42, 39,45, 41]
res = list(filter(lambda i : i > 40, temp))
print(res)

#4. Identify Prime Numbers (Recursion)
n = int(input("Enter the number: "))
c = 0
for i in range(2, n // 2 + 1):
    if n % i == 0:
        c += 1
        break

if c == 0:
    print("Prime Number")
else:
    print("Not a Prime Number")

#OR
def is_prime(n):
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True

n = int(input("Enter the Number: "))
print(is_prime(n))

#5. Reverse Digits(Recursion)
def reverse_number(n):
    if n == 0:
        return
    print(n % 10, end =' ')
    reverse_number(n // 10)

reverse_number(1234)
reverse_number(450)

#6. Filter by Starting Letter
inp = ["cat", "car", "bat", "apple"]
ch = 'c'
res = list(filter(lambda i: i.startswith(ch), inp))
print(res)

#7. Create Your Own Utility Module(User-Defined Modules)
def is_palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

def capitalize_words(text):
    return text.capitalize()

#main.py
print(is_palindrome("madam"))
print(capitalize_words("hello world"))

#8. Remove Duplicates Case-insensitive(Set + Lambda)
words = ["Apple", "apple", "Banana", "banana", "Cheery", "cherry"]
res = set(map(lambda i : i.lower(), words))
print(res)

#9. Countdown Timer(Generator)
def countdown(n):
    for i in range(n, -1, -1):
        yield i

n = int(input())
c = countdown(n)
for i in range(n + 1):
    print(next(c))

#10. Nested Sum(lst)
def nested_sum(n):
    total = 0
    for i in n:
        if isinstance(i, list):
            total += nested_sum(i)
        else:
            total += i
    return total
print(nested_sum([[1, 2], [3, [4, 5]]]))
