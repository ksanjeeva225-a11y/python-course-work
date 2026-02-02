'''
input formatting
'''

# String input
i = input("enter the string: ")
print(i)

# Integer input
i = int(input("enter the value: "))
print(i)

# Float input
p = float(input("enter the value: "))
print(p)

# Split into list of strings
l = input("enter the values: ").split()
print(l)

# Split by comma
l = input("enter the values: ").split(",")
print(l)

# List of integers
s = list(map(int, input("enter the values: ").split()))
print(s)

# List of floats
s = list(map(float, input("enter the values: ").split()))
print(s)

# List of tuples (each word becomes a tuple of characters)
s = list(map(tuple, input("enter the values: ").split()))
print(s)

# List of sets (each word becomes a set of characters)
s = list(map(set, input("enter the values: ").split()))
print(s)

# Tuple of integers
s = tuple(map(int, input("enter the values: ").split()))
print(s)

# Tuple of floats
s = tuple(map(float, input("enter the values: ").split()))
print(s)

# Tuple of lists (each word becomes a list of characters)
s = tuple(map(list, input("enter the values: ").split()))
print(s)

# Set of integers
p = set(map(int, input("Enter selected image IDs: ").split()))
print(p)

# eval() – takes Python literals (use carefully!)
p = eval(input("values: "))
print(p)


'''
multiple packing & unpacking
'''
username, email = input("Enter username and password: ").split()
print("Username:", username)
print("email:", email)
