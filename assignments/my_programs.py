# Python Function Bank

def sum_two_numbers():
    print("Program: Sum of Two Numbers")
    print("""
def sum(a, b):
    return a + b
""")
    print("Test Case 1: sum(10, 20) -> 30")
    print("Test Case 2: sum(-5, 7) -> 2")
    print("Explanation: Adds two numbers using the + operator.")


def even_odd():
    print("Program: Even or Odd")
    print("""
def even_odd(n):
    if n % 2 == 0:
        return 'Even'
    else:
        return 'Odd'
""")
    print("Test Case 1: even_odd(4) -> Even")
    print("Test Case 2: even_odd(7) -> Odd")
    print("Explanation: Uses modulo operator to check divisibility by 2.")


def factorial():
    print("Program: Factorial of a Number")
    print("""
def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact
""")
    print("Test Case 1: factorial(5) -> 120")
    print("Test Case 2: factorial(0) -> 1")
    print("Explanation: Multiplies numbers from 1 to n using a loop.")


def prime_check():
    print("Program: Prime Number Check")
    print("""
def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
""")
    print("Test Case 1: is_prime(7) -> True")
    print("Test Case 2: is_prime(9) -> False")
    print("Explanation: Checks if number has divisors other than 1 and itself.")


def reverse_string():
    print("Program: Reverse a String")
    print("""
def reverse(s):
    return s[::-1]
""")
    print("Test Case 1: reverse('Python') -> 'nohtyP'")
    print("Test Case 2: reverse('abc') -> 'cba'")
    print("Explanation: Uses string slicing with step -1.")


def palindrome():
    print("Program: Palindrome Check")
    print("""
def is_palindrome(s):
    return s == s[::-1]
""")
    print("Test Case 1: is_palindrome('madam') -> True")
    print("Test Case 2: is_palindrome('hello') -> False")
    print("Explanation: Compares string with its reverse.")


def count_vowels():
    print("Program: Count Vowels")
    print("""
def count_vowels(s):
    count = 0
    for ch in s:
        if ch in 'aeiouAEIOU':
            count += 1
    return count
""")
    print("Test Case 1: count_vowels('Python') -> 1")
    print("Test Case 2: count_vowels('Education') -> 5")
    print("Explanation: Iterates through string and counts vowels.")


def largest_of_three():
    print("Program: Largest of Three Numbers")
    print("""
def largest(a, b, c):
    return max(a, b, c)
""")
    print("Test Case 1: largest(3, 7, 5) -> 7")
    print("Test Case 2: largest(-1, -4, -2) -> -1")
    print("Explanation: Uses built-in max() function.")


def sum_of_digits():
    print("Program: Sum of Digits")
    print("""
def sum_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total
""")
    print("Test Case 1: sum_digits(123) -> 6")
    print("Test Case 2: sum_digits(99) -> 18")
    print("Explanation: Extracts digits using modulo and adds them.")


def fibonacci():
    print("Program: Fibonacci Series")
    print("""
def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a)
        a, b = b, a+b
""")
    print("Test Case 1: fibonacci(5) -> 0 1 1 2 3")
    print("Test Case 2: fibonacci(7) -> 0 1 1 2 3 5 8")
    print("Explanation: Each term is sum of previous two numbers.")


def gcd():
    print("Program: GCD of Two Numbers")
    print("""
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
""")
    print("Test Case 1: gcd(12, 18) -> 6")
    print("Test Case 2: gcd(7, 5) -> 1")
    print("Explanation: Uses Euclidean algorithm.")


def lcm():
    print("Program: LCM of Two Numbers")
    print("""
def lcm(a, b):
    return (a * b) // gcd(a, b)
""")
    print("Test Case 1: lcm(4, 6) -> 12")
    print("Test Case 2: lcm(5, 7) -> 35")
    print("Explanation: Uses GCD to calculate LCM.")


def decimal_to_binary():
    print("Program: Decimal to Binary")
    print("""
def dec_to_bin(n):
    return bin(n)[2:]
""")
    print("Test Case 1: dec_to_bin(10) -> 1010")
    print("Test Case 2: dec_to_bin(7) -> 111")
    print("Explanation: Uses Python's bin() function.")


def count_words():
    print("Program: Count Words in a String")
    print("""
def count_words(s):
    return len(s.split())
""")
    print("Test Case 1: count_words('Hello World') -> 2")
    print("Test Case 2: count_words('Python is fun') -> 3")
    print("Explanation: Splits string and counts words.")


def multiplication_table():
    print("Program: Multiplication Table")
    print("""
def table(n):
    for i in range(1, 11):
        print(n, 'x', i, '=', n*i)
""")
    print("Test Case 1: table(5) -> 5x1 to 5x10")
    print("Test Case 2: table(3) -> 3x1 to 3x10")
    print("Explanation: Uses loop to print table.")


def leap_year():
    print("Program: Leap Year Check")
    print("""
def is_leap(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0
""")
    print("Test Case 1: is_leap(2024) -> True")
    print("Test Case 2: is_leap(2023) -> False")
    print("Explanation: Applies leap year conditions.")


def power():
    print("Program: Power of Number")
    print("""
def power(a, b):
    return a ** b
""")
    print("Test Case 1: power(2, 3) -> 8")
    print("Test Case 2: power(5, 2) -> 25")
    print("Explanation: Uses exponentiation operator.")


def area_circle():
    print("Program: Area of Circle")
    print("""
def area(r):
    return 3.14 * r * r
""")
    print("Test Case 1: area(7) -> 153.86")
    print("Test Case 2: area(5) -> 78.5")
    print("Explanation: Uses formula πr².")


def simple_interest():
    print("Program: Simple Interest")
    print("""
def si(p, r, t):
    return (p * r * t) / 100
""")
    print("Test Case 1: si(1000, 5, 2) -> 100")
    print("Test Case 2: si(5000, 4, 1) -> 200")
    print("Explanation: Uses simple interest formula.")


def temperature_conversion():
    print("Program: Celsius to Fahrenheit")
    print("""
def c_to_f(c):
    return (c * 9/5) + 32
""")
    print("Test Case 1: c_to_f(0) -> 32")
    print("Test Case 2: c_to_f(100) -> 212")
    print("Explanation: Converts Celsius to Fahrenheit.")