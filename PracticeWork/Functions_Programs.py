#1. Add Two Numbers
def addition(a,b):
    return a+b
num1=int(input())
num2=int(input())
result=addition(num1,num2)
print(result)

#2. Square a Number
def square(n):
    return n**2
#n=int(input())
print(square(7))

#3. Area of a Circle
def area(r):
    return 3.14*r*r
r=int(input())
print(area(r))

#4. Greet the User
def greet(name):
    print(f"Hello, {name}")
name=input("Enter your name:")
print(greet(name))

#5. Convert Celsius to Fahrenheit
def con(c):
    return (c*9/5)+32
    print(f"Temperature in Fahrenheit:{f}")
c=float(input("Enter temperature in Celsius:"))
f=con(c)
print(f)

#6. Multiply Three Numbers
def mul(a,b,c):
    return a*b*c
a=int(input())
b=int(input())
c=int(input())
print(mul(a,b,c))

#7. Calculate Simple Interest
def simple_interest(p,t,r):
    si=(p*t*r)/100
    return si
p=float(input())
t=float(input())
r=float(input())
print(simple_interest(p,t,r))

#8. Find Length of a String
def length(s):
    count=0
    for i in s:
        count+=1
    return count
s="python"
print(length(s))

#9. Append to a List
def append_item(lst, item):
    lst.append(item)
    return lst
lst=list(map(int, input().split()))
ele=int(input())
updated_list=append_item(lst, ele)
print(updated_list)  

#10. Double Each Element in a List
l=list(map(int,input().split()))
double=list(map(lambda i:i*2,l))
print(double)      

#11. Sort a List
def sort_l(lst):
    return sorted(lst)
l=list(map(int,input().split()))
print(sort_l(l))

#12. Clear a List Inside Function
def clear_list(lst):
    lst.clear()
    return lst
l=list(map(int,input().split()))
print(clear_list(l))

#13. Update Dictionary Value
def update_value(d, key, new_value):
    d[key] = new_value
    return d
dictionary = eval(input("Enter dictionary: "))
key = input("Enter key to update: ")
new_value = eval(input("Enter new value: "))
print(update_value(dictionary, key, new_value))

#14. Remove Element from List by Value
def remove_ele(l,ele):
    l.remove(ele)
    return
l=list(map(int,input().split()))
print(remove_ele(1,3))

#15. Add Key to Dictionary
def add_key(d, key, value):
    d[key] = value
    return d
dictionary = eval(input("Enter dictionary: "))
new_key = input("Enter new key: ")
new_value = eval(input("Enter new value: "))
print(add_key(dictionary, new_key, new_value))

#16. Increment All Values in Dictionary
def update(d):
    for i in d:
        d[i]+=1
    return d
d={'a':7,"b":4,'c':4}
print(update(d))

#17. Factorial of a Number
def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact=fact*i
    return fact
print(factorial(6))

#18. Fibonacci Number (Nth Term)
def fibonacci(n):
    a,b = 0,1
    res=[]
    for i in range(n):
        res.append(a)
        a,b=b,a+b
    return res
n=int(input())
print(factorial(n))

#19. Sum of First N Natural Numbers
def sum_n(n):
    return n*(n+n)//2
n=int(input())
print(sum_n(n))

#20. Reverse a String Using Recursion
def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return s[-1] + reverse_string(s[:-1])
s = input("Enter a string: ")
print(reverse_string(s))

#21. Power of a Number (a^b using recursion)
def power(a, b):
    if b == 0:
        return 1
    else:
        return a * power(a, b - 1)
a = int(input("Enter base (a): "))
b = int(input("Enter exponent (b): "))
print(power(a, b))

#22. Sum of Digits Using Recursion
def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_of_digits(n // 10)
n = int(input("Enter a number: "))
print(sum_of_digits(n))

#23. Check Palindrome String Using Recursion
def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])
s = input("Enter a string: ")
print(is_palindrome(s))

#24. GCD of Two Numbers Using Recursion
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(gcd(a, b))

#25. Maximum of Three Numbers Using max()
def max_of_three(a, b, c):
    return max(a, b, c)
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
print(max_of_three(a, b, c))

#26. Sort a List Using sorted()
def sort_list(lst):
    return sorted(lst)
lst = list(map(int, input("Enter list elements separated by space: ").split()))
print(sort_list(lst))

#27. Sum of Elements Using sum()
def sum_of_elements(lst):
    return sum(lst)
lst = list(map(int, input("Enter list elements separated by space: ").split()))
print(sum_of_elements(lst))

#28. Find Data Type Using type()
def find_data_type(var):
    return type(var)
var = eval(input("Enter a variable: "))
print(find_data_type(var))

#29. Print Even Numbers up to N
def print_even_numbers(n):
    for i in range(2, n + 1, 2):
        print(i, end=' ')
n = int(input("Enter a number: "))
print_even_numbers(n)

#30. Return List of Squares
def list_of_squares(n):
    return [i**2 for i in range(1, n + 1)]
n = int(input("Enter a number: "))
print(list_of_squares(n))

#31. Check if Number is Prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
n = int(input("Enter a number: "))
print(is_prime(n))

#32. Count Vowels in a String
def count_vowels(s):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count
s = input("Enter a string: ")
print(count_vowels(s))

#33. Multiply by 2 Using Lambda
multiply_by_2 = lambda x: x * 2
n = int(input("Enter a number: "))
print(multiply_by_2(n))

#34. Filter Even Numbers Using Lambda
filter_even = lambda lst: list(filter(lambda x: x % 2 == 0, lst))
lst = list(map(int, input("Enter list elements separated by space: ").split()))
print(filter_even(lst))

#35. Filter Even Numbers Using filter() and Lambda
def filter_even_numbers(lst):
    return list(filter(lambda x: x % 2 == 0, lst))
lst = list(map(int, input("Enter list elements separated by space: ").split()))
print(filter_even_numbers(lst))

#36. Sort Tuples by Second Value Using Lambda
def sort_tuples(tuples_list):
    return sorted(tuples_list, key=lambda x: x[1])
tuples_list = [(1, 3), (4, 1), (5, 2)]
print(sort_tuples(tuples_list))

#37. Access Global Variable Inside Function
x = 10
def access_global():
    global x
    return x
print(access_global())

#38. Modify Global Variable Inside Function
y = 5
def modify_global():
    global y
    y += 10
    return y
print(modify_global())

#39. Use Local Variable with Same Name as Global
z = 20
def local_variable():
    z = 15
    return z
print(local_variable())
print(z)

#40. Compare Global and Local Variables
x = 10
def compare_variables():
    x = 20
    print("Local x:", x)
compare_variables()
print("Global x:", x)
