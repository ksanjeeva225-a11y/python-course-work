'''
Q1. The Birthday Format Fixer (String & Type Conversion)
Ravi is building a birthday reminder system. He receives the birthday input from users as a
string in the format dd-mm-yyyy, but he needs to store it in the format yyyy/mm/dd. Write
a program that takes a birthday as input and outputs it in the correct format.
Input
A string representing a date: dd-mm-yyyy
Output
A string formatted as: yyyy/mm/dd
Test Cases

Input: 17-07-2025
Output: 2025/07/17
Input: 01-01-2000
Output: 2000/01/01
'''
date_input = input("Enter your birthday (dd-mm-yyyy): ")
day, month, year = date_input.split('-')
print(f"{year}/{month}/{day}")

'''
Q2. The Even Odd Game (Conditional Statement)
A number-guessing game gives points based on whether a number is even or odd. You need
to write a program that takes an integer and prints:
● "Even Winner" if it's even
● "Odd Winner" if it's odd
Input
An integer n
Output
"Even Winner" or "Odd Winner"
'''
n = int(input("Enter a number: "))
if n % 2 == 0:
    print("Even Winner")
else:
    print("Odd Winner")

'''
Q3. Vowel Replacer Bot (String Methods)
A chatbot is trying to censor all vowels in its messages with a *. Write a Python program that
reads a message string and replaces all lowercase vowels with *.
Input
A string msg
Output
Modified string with vowels replaced by *
Test Cases

Input: hello world
Output: h*ll* w*rld
Input: python is fun
Output: pyth*n *s f*n
'''
s = input("Enter a message: ")
vowels = 'aeiou'
censored_msg = ''.join('*' if char.lower() in vowels else char for char in s)
print(censored_msg)

'''
Q4. Shopping Cart Analyzer (List Operations)
In a shopping app, a list holds the prices of items added to the cart. Write a program to input
a list of item prices and calculate the total price and the maximum item price.
Input
List of floats separated by space (e.g. 12.5 7.99 3.5)
Output
Two lines”
1. Total price
2. Maximum price
Test Cases

Input: 10.5 20.0 5.5
Output:
36.0
20.0
Input: 100.0 50.0
Output:
150.0
100.0
'''
prices = list(map(float, input("Enter item prices separated by space: ").split()))
total_price = sum(prices)
max_price = max(prices)
print(total_price)
print(max_price)

'''
Q5. Secure Login System (Tuple & Conditional)
You’re asked to write a login checker where the stored username and password are inside a
tuple. Your program will input a username and password from the user and compare it with
the stored values to print "Login Successful" or "Access Denied".
Stored Credentials

credentials = ("admin", "python123")

Input
Two strings: username and password
Output
Login Successful / Access Denied
Test Cases

Input:
admin
python123
Output: Login Successful
Input:
admin
wrongpass
Output: Access Denied
'''
credentials = ("admin", "python123")
username = input("Enter username: ")
password = input("Enter password: ")
if (username, password) == credentials:
    print("Login Successful")
else:
    print("Access Denied")

'''
Q6. Remove Duplicates from Set (Set Operations)
A form collects student names, but due to error, some students have entered their names
more than once. You are to clean up the data using a set.
Input
A string of names separated by commas (e.g., "Asha,Ravi,Ravi,John,Asha")
Output
Print a sorted list (alphabetical) of unique names
Test Cases

Input: Ravi,Asha,Asha,John
Output: ['Asha', 'John', 'Ravi']
Input: Meena,Arun,Arun,Ravi
Output: ['Arun', 'Meena', 'Ravi']
'''
names_input = input("Enter names separated by commas: ")
names = set(names_input.split(','))
print(sorted(names))

'''
Q7. Student Marks Record (Dictionary Operations)
You’re developing a student mark tracker. Write a program to:
1. Input number of students n
2. For each student, take name and marks
3. Store them in a dictionary
4. Print the student with the highest marks

Input
First line: integer n
Next n lines: name and marks (separated by space)
Output
Name of student with highest marks

Python

Python
Test Cases

Input:
3
Ravi 85
Anu 90
Sita 88
Output: Anu
Input:
2
Rahul 70
Meena 75
Output: Meena
'''
n = int(input(" "))
marks_dict = {}
for i in range(n):
    entry = input(" ").split()
    name = entry[0]
    marks = int(entry[1])
    marks_dict[name] = marks
print(max(marks_dict, key=marks_dict.get))

'''
Q8. Reverse My Words (String Slicing)
You need to create a feature for a language learning app where it shows each word in a
sentence in reverse. Keep the word order the same but reverse each word.
Input
A string sentence
Output
Each word reversed, separated by space
Test Cases

Input: hello world
Output: olleh dlrow
Input: python is fun
Output: nohtyp si nuf
'''
sentence = input("Enter a sentence: ")
words = sentence.split()
reversed_words = [word[::-1] for word in words]
print(" ".join(reversed_words))

'''
Q9. Clean My List (List and Type Conversion)
From user input, you receive values as strings representing numbers (e.g., "12 14 0 7").
Your job is to:
● Convert them to integers
● Remove all zeros
● Print the cleaned list
Input
String of numbers separated by space
Output
List of non-zero integers
Test Cases

Input: 10 0 5 0 3
Output: [10, 5, 3]
Input: 0 0 1
Output: [1]
'''
nums=list(map(int,input().split()))

while 0 in nums:
    nums.remove(0)

print(nums)

'''
Q10. The Frequency Counter (Dictionary + String)
Write a program that takes a string and counts the frequency of each character (excluding
spaces) and prints the dictionary of character counts.
Input
A single-line string
Output
A dictionary with characters as keys and their counts as values
Test Cases

Input: hello world
Output: {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}
Input: a b a
Output: {'a': 2, 'b': 1}
'''
s = input("").replace(" ", "")
freq_dict = {}
for char in s:
    freq_dict[char] = freq_dict.get(char, 0) + 1
print(freq_dict)
