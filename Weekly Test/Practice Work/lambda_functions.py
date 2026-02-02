#1. Square of a number using lambda
square = lambda x: x ** 2
# Test Cases
print(square(4))  # Output: 16
print(square(7))  # Output: 49

#2. Check if number is even using lambda
is_even = lambda x: x % 2 == 0
# Test Cases
print(is_even(6))  # Output: True
print(is_even(5))  # Output: False

#3. Get maximum of two numbers using lambda
max_num = lambda x, y: x if x > y else y
# Test Cases
print(max_num(4, 9))  # Output: 9
print(max_num(7, 3))  # Output: 7

#4. Multiply two numbers using lambda
multiply = lambda x, y: x * y
# Test Cases
print(multiply(2, 5))  # Output: 10
print(multiply(4, 3))  # Output: 12

#5. Sort a list of tuples by second element using lambda
data1 = [(1, 3), (2, 1), (4, 2)]
data2 = [(5, 10), (3, 7), (8, 1)]
# Sorting using lambda
sorted_data1 = sorted(data1, key=lambda x: x[1])
sorted_data2 = sorted(data2, key=lambda x: x[1])
# Test Cases
print(sorted_data1)  # Output: [(2, 1), (4, 2), (1, 3)]
print(sorted_data2)  # Output: [(8, 1), (3, 7), (5, 10)]

#6. Filter even numbers from a list using lambda and filter()
list1 = [1, 2, 3, 4, 5, 6]
list2 = [10, 15, 22]
# Using lambda with filter to get even numbers
even_numbers1 = list(filter(lambda x: x % 2 == 0, list1))
even_numbers2 = list(filter(lambda x: x % 2 == 0, list2))
# Test Cases
print(even_numbers1)  # Output: [2, 4, 6]
print(even_numbers2)  # Output: [10, 22]

#7. Square each element in a list using lambda and map()
list1 = [1, 2, 3]
list2 = [4, 5, 6]
# Using lambda with map to square elements
squares1 = list(map(lambda x: x ** 2, list1))
squares2 = list(map(lambda x: x ** 2, list2))
# Test Cases
print(squares1)  # Output: [1, 4, 9]
print(squares2)  # Output: [16, 25, 36]

#8. Convert list of strings to uppercase using lambda
list1 = ["hello", "world"]
list2 = ["python", "lambda"]
# Using lambda with map to convert strings to uppercase
uppercase1 = list(map(lambda x: x.upper(), list1))
uppercase2 = list(map(lambda x: x.upper(), list2))
# Test Cases
print(uppercase1)  # Output: ["HELLO", "WORLD"]
print(uppercase2)  # Output: ["PYTHON", "LAMBDA"]

#9. Sort list of dictionaries by key using lambda
data1 = [{'name': 'A', 'age': 30}, {'name': 'B', 'age': 20}]
data2 = [{'age': 25}, {'age': 18}]

sorted_data1 = sorted(data1, key=lambda x: x['age'])
sorted_data2 = sorted(data2, key=lambda x: x['age'])
print(sorted_data1) # Output: [{'name': 'B', 'age': 20}, {'name': 'A', 'age': 30}]
print(sorted_data2) # Output: [{'age': 18}, {'age': 25}]

#10. Return length of a string using lambda
string_length = lambda s: len(s)

# Test Cases
print(string_length("hello"))   # Output: 5
print(string_length("python"))  # Output: 6

#11. Check if string starts with a vowel using lambda
starts_with_vowel = lambda s: s[0].lower() in 'aeiou'
# Test Cases
print(starts_with_vowel("apple"))   # Output: True
print(starts_with_vowel("banana"))  # Output: False

#12. Add 10 to each element using lambda and map()
list1 = [1, 2, 3]
list2 = [5, 0, -2]

# Using lambda with map to add 10 to each element
added10_list1 = list(map(lambda x: x + 10, list1))
added10_list2 = list(map(lambda x: x + 10, list2))

# Test Cases
print(added10_list1)  # Output: [11, 12, 13]
print(added10_list2)  # Output: [15, 10, 8]

#13. Filter strings longer than 3 characters
list1 = ["a", "the", "lamp", "cat"]
list2 = ["sun", "sky", "tree"]

long_strings1 = list(filter(lambda s: len(s) > 3, list1))
long_strings2 = list(filter(lambda s: len(s) > 3, list2))

# Test Cases
print(long_strings1)  # Output: ["lamp"]
print(long_strings2)  # Output: ["tree"]

#14. Multiply each number by its index using lambda
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7]
result1 = list(map(lambda x: x[0] * x[1], enumerate(list1)))
result2 = list(map(lambda x: x[0] * x[1], enumerate(list2)))

# Test Cases
print(result1)  # Output: [0, 2, 6, 12]
print(result2)  # Output: [0, 6, 14]

#15. Use lambda with reduce() to calculate product
from functools import reduce
list1 = [1, 2, 3, 4]
list2 = [2, 5, 5]

product1 = reduce(lambda x, y: x * y, list1)
product2 = reduce(lambda x, y: x * y, list2)

# Test Cases
print(product1)  # Output: 24
print(product2)  # Output: 50

#16. Use lambda with filter to find multiples of 3
list1 = [1, 3, 4, 6, 9]
list2 = [5, 10, 12, 15]

multiples_of_3_1 = list(filter(lambda x: x % 3 == 0, list1))
multiples_of_3_2 = list(filter(lambda x: x % 3 == 0, list2))

# Test Cases
print(multiples_of_3_1)  # Output: [3, 6, 9]
print(multiples_of_3_2)  # Output: [12, 15]

#17. Sort words in a list by their length
list1 = ["car", "elephant", "cat"]
list2 = ["hi", "world", "python"]

sorted_list1 = sorted(list1, key=lambda x: len(x))
sorted_list2 = sorted(list2, key=lambda x: len(x))

# Test Cases
print(sorted_list1)  # Output: ["car", "cat", "elephant"]
print(sorted_list2)  # Output: ["hi", "world", "python"]

#18. Lambda to extract domain from email
extract_domain = lambda email: email.split('@')[1]

# Test Cases
print(extract_domain("user@gmail.com"))  # Output: "gmail.com"
print(extract_domain("name@yahoo.com"))  # Output: "yahoo.com"

#19. Use lambda to get last digit of a number
last_digit = lambda x: x % 10

# Test Cases
print(last_digit(123))  # Output: 3
print(last_digit(7890))  # Output: 0

#20. Use lambda to check if year is a leap year
is_leap_year = lambda year: (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Test Cases
print(is_leap_year(2020))  # Output: True
print(is_leap_year(2023))  # Output: False
