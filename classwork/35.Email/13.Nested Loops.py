for j in range(3):
    for i in range(5):
        print('*', end = ' ')
    print()

for row in range(4):
    for col in range(4):
        print('*', end = ' ')
    print()

for row in range(5):  
    for col in range(5):  
        print(row, end=' ')  
    print()

for row in range(5):  
    for col in range(5):  
        print(col, end=' ')  
    print()

for row in range(5):  
    for col in range(row + 1):  
        print(col, end=' ')  
    print()

n = int(input("Enter the size: "))
        
for row in range(n):  
    for col in range(n - row):  
        print(col, end=' ')  
    print()

n = int(input("Enter the size: "))

for row in range(n):
    for space in range(n - 1 - row):
        print(' ', end=' ')
    for col in range(row + 1):
        print('*', end=' ')
        
    print()

n = int(input("Enter the size: "))

for row in range(n):
    for space in range(row):
        print(' ', end=' ')
    for col in range(n - row):
        print('*', end=' ')
        
    print()

n = int(input("Enter the size: "))

for row in range(n):
    for col in range(n):
        if row == 0 or row == n - 1 or col == 0 or col == n - 1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()


n = int(input("Enter the size: "))

for row in range(n):
    if row % 2 == 0:  
        for col in range(n):
            print('*', end=' ')
    else:
        for col in range(n):
            if col == 0 or col == n - 1:
                print('*', end=' ')
            else:
                print(' ', end=' ')
    print()

n = int(input("Enter the size: "))

for row in range(n):
    for col in range(n):
        if row == 0 or row == n - 1 or col == n - 1 - row:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()

# Draw an X pattern
'''
*       * 
  *   *   
    *     
  *   *   
*       * 
'''
n = int(input("Enter the size: "))

for row in range(n):
    for col in range(n):
        if row == col or col == n - 1 - row:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()


#. For Alternate Numbers
'''
1 0 1 0 1
1 0 1 0 1
1 0 1 0 1
1 0 1 0 1
1 0 1 0 1
'''
n = int(input("Enter the size: "))

for i in range(n):
    for j in range(n):
        if j % 2 == 0:
            print(1, end=' ')
        else:
            print(0, end=' ')
    print()

#. Reverse the above one
'''
0 1 0 1 0
0 1 0 1 0
0 1 0 1 0
0 1 0 1 0
0 1 0 1 0
'''
n = int(input("Enter the size: "))

for i in range(n):
    for j in range(n):
        print(j % 2, end=' ')

    print()

#. Negative Values
'''
-1 -2 -1 -2 -1
-1 -2 -1 -2 -1
-1 -2 -1 -2 -1
-1 -2 -1 -2 -1
-1 -2 -1 -2 -1
'''
n = int(input("Enter the size: "))

for i in range(n):
    for j in range(n):
        print(~(j % 2), end=' ')

    print()

#. Boolean values
'''
True False True False True 
True False True False True 
True False True False True 
True False True False True 
True False True False True 
'''
n = int(input("Enter the size: "))

for i in range(n):
    for j in range(n):
        print(not (j % 2), end=' ')

    print()

#. 0 and 1 Right-Inverted triangle
'''
1 0 0 0 0 
1 1 0 0 0 
1 1 1 0 0 
1 1 1 1 0 
1 1 1 1 1 
'''
n = int(input("Enter the size: "))

for i in range(n):
    for j in range(n):
        if i < j:
            print(0, end =' ')
        else:
            print(1, end =' ')
    print()
    
#. House Roof Pattern
'''
    *     
  *   *   
* * * * * 
*       * 
*       * 
'''
n = int(input("Enter the size: "))

for i in range(n):
    for j in range(n):
        if i == n // 2 or (j == 0 and i > n // 2) or (j == n - 1 and i > n // 2) or (i + j == n // 2 and i < n // 2) or (j - i == n // 2 and i < n // 2):
            print('*', end =' ')
        else:
            print(' ', end =' ')
    print()
