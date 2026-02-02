'''
List comprehension

# Basic Syntax
c = [res for i in seq]

'''
l = []
for i in range(1, 11):
    l.append(i)

print(l)

c = [i for i in range(1, 11)]
print(c)

#Even numbers
c = [i for i in range(2, 101, 2)]
print(c)

# Square Numbers
c = [i**2 for i in range(1, 11)]
print(c)

# Print Vowels

vol = 'aeiouAEIOU'

sen = input("Enter the sen: ")

r = [i for i in sen if i in vol]

print(r)

# '*' pattern

r = ['*' if i % 2 == 0 else 0 for i in range(5)]
print(r)

# Other format
t = tuple(i for i in range(10))
s = {i for i in range(10)}
l = {i for i in range(10)}
d = {i: i*i for i in range(10)}

print(t, s, d, sep='\n')
