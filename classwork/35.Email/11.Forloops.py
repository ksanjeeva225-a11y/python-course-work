'''

for var in seq:
    #stmts

for var in enumerate(seq):
    #stnts

for i in range(start, end + 1, step):
    #stmt

for i in range(len(seq)):
    #stmts
    
Seq: lists, tuple, set, dict, str, range()
'''
#1. List
lang = ['python','java', 'c', 'c++', 'mysql', 'ds', 'flask', 'javascript']

for i in lang:
    print(i)

for i in  enumerate(lang):
    print(i,i[0],i[1])

#2. Tuple
lang = ('python','java', 'c', 'c++', 'mysql', 'ds', 'flask', 'javascript')

for i in lang:
    print(i)

for i in  enumerate(lang):
    print(i,i[0],i[1])

#3. Set
lang = {'python','java', 'c', 'c++', 'mysql', 'ds', 'flask', 'javascript'}

for i in lang:
    print(i)

#4. Dict
lang = {
    1: 'python', 2: 'java', 3: 'c', 4: 'c++',
    5: 'mysql', 6: 'ds', 7: 'flask', 8: 'javascript'
}

for i in lang:
    print(f'key-{i} value-{lang[i]}')

for index, key in enumerate(lang):
    print(f'index-{index} key-{key} value-{lang[key]}')

#5. String
lang = 'python programming'

for i in lang:
    print(f'{i}')

for i in  enumerate(lang):
    print(f'index-{i[0]} val-{i[1]}')

#6. Range()
for i in range(1, 11):
    print(i)

# Odd
for i in range(1,101,2):
    print(i)

#From User table
num = int(input("Enter the number: "))
for i in range(1, 21):
    print(f'{num} * {i} = {num * i}')

# Reverse of Seq
for i in range(3,100,3):
    print(i)

#iterate the list using range
l = ['laptop', 'mouse', 'charger', 'keyboard']
for i in range(len(l)):
    print(i, l[i])

l = 'string'
for i in range(len(l)):
    print(i, l[i])
