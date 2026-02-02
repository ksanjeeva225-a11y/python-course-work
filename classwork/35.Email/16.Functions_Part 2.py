'''
Pass By Values and References Functions
'''
def update(n):
    n += 10
    print("Inside: ",n)

n = 10
update(n)
print("Ouside: ", n)

#String
def update(n):
    n += "Programming"
    print("Inside: ",n)

n = "Python"
update(n)
print("Ouside: ", n)

# List
def update(n):
    n.append(5)
    print("Inside: ",n)

n = [1, 2, 3, 4]
update(n)
print("Ouside: ", n)

#tuple
def update(n):
    n += (5,)
    print("Inside: ",n)

n = (1, 2, 3, 4)
update(n)
print("Ouside: ", n)

#set
def update(n):
    n.add(5)
    print("Inside: ",n)

n = {1, 2, 3, 4}
update(n)
print("Ouside: ", n)


#dict
def update(n):
    n[5] = 25
    print("Inside: ",n)

n = {1: 1, 2: 4, 3: 9, 4: 16}
update(n)
print("Ouside: ", n)

#. Memory allocations
def update(n):
    n[5] = 25
    print("Inside: ",n, id(n))

n = {1: 1, 2: 4, 3: 9, 4: 16}
update(n)
print("Ouside: ", n, id(n))

# Shallow copy
def update(n):
    n = n.copy()
    n.append(5)
    print("Inside: ",n, id(n))

n = [1, 2, 3, 4]
update(n)
print("Ouside: ", n, id(n))

'''
Recursive functions
'''

def shooting(bullets):
    if bullets <= 0:
        print("Game Over")
        return
    print(f'{bullets} bullets left')
    shooting(bullets - 1) 

shooting(10)

# Print 1 - 10 numbers using recursive
def display(n):
    if n > 10:
        print("Exit")
        return
    print(n)
    display(n + 1)
display(1)
# Reverse
def display(n):
    if n > 10:
        print("Exit")
        return
    display(n + 1)
    print(n)
display(1)

#List
def display(n, i):
    if i >= len(n):
        print("Exit")
        return
    print(n[i])
    display(n, i + 1)
    
display("Codegnan", 0)

def display(n, i):
    if i >= len(n):
        print("Exit")
        return
    display(n, i + 1)
    print(n[i])
    
display("Codegnan", 0)

'''
abcde

a
ab
abc
abcd
abcde
'''
def display(n, i):
    if i >= len(n):  
        print("Exit")
        return
    print(n[:i+1])  
    display(n, i + 1)  

display("abcde", 0)

'''
abc
abcabc
abcabcabc
'''
def display(pattern, i, n):
    if i > n:
        print("Exit")
        return
    
    print(pattern * i)
    display(pattern, i + 1, n)

display("abc", 1, 3)

'''
abcdefgh 3
abc
bcd
cde
def
fgh

abcdefgh 4
abcd
bcde
cdef
defh
efgh
'''
def display(s, k, i=0):
    if i + k > len(s):
        print("Exit")
        return

    print(s[i:i+k])
    display(s, k, i + 1)


display("abcdefgh", 3)  
display("abcdefgh", 4)
