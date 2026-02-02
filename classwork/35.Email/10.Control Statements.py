'''

In Python, the main types of conditional statements are:
1. if Statement
2. if-else Statement
3. if-elif-else Statement
4. Nested Conditional Statements

if condition:
      #stmts

if - else

if - elif ..... - else

if if-elif-ele-else

'''
'''
#1. Simple if

send = False
if send:
    print("Send the message")


followers = []
click = True
if click:
    followers.append("user1")

data = {
    'ajay@gmail.com': '1234',
    'saikrishna@gmail.com': '5678',
    'prasad@gmail.com': '2222',
    'tejaswini@gmail.com': '9876'
}

mail = input("Enter the mail: ")
pwd = input("Enter the password: ")

if data.get(mail) == pwd:
    print("Valid Login")
else:
    print("Invalid Login")

'''
#2. if-elif-else

amount = int(input("Enter the amount: "))
actual_amount = amount

if amount >= 10000:
    actual_amount = amount - amount * 0.5

elif 8000 <= amount <10000:
    actual_amount = amount - amount * 0.3
    
elif 5000 <= amount < 8000:
    actual_amount = amount - amount * 0.2

elif 2000 <= amount < 5000:
    actual_amount = amount - amount * 0.05

print(f"Amount: {amount}\nAfter discount: {actual_amount}")

budget = int(input("Enter the budget: "))

if budget > 20000:
    print("Trip to Goa")

elif 15000 <= budget <= 20000:
    print("Go for Shopping")

elif 10000 <= budget < 15000:
    print("Clubbing")

elif 5000 <= budget < 10000:
    print("Go for Cafe")

elif 2000 <= budget < 5000:
    print("Go for movie")

elif 1000 <= budget < 2000:
    print("Go for Temple")

elif 500 <= budget < 1000:
    print("Save Money")

elif 100 <= budget < 500:
    print("No Trip")

#3. Nested if-else
data = {
    1:'Satish will Sing',
    2:'Telugu Dialog - Krishna',
    3:'Imran will Give Party',
    4:'Ask a question - Ajay',
    5:'Ramp Walk - Teja',
    6:'Anything - Sumanth'
}

char = input("Enter a character (a-f): ")

if char == 'a':
    key = 1
elif char == 'b':
    key = 2
elif char == 'c':
    key = 3
elif char == 'd':
    key = 4
elif char == 'e':
    key = 5
elif char == 'f':
    key = 6
else:
    print("Invalid character")
    key = None

if key:
    print(data[key])

products = ['laptop', 'mouse', 'phone', 'keyboard', 'charger', 'speaker']
stocks = [100, 20, 500, 0, 200, 6]

print("*" * 30)
print(products)
print("*" * 30)

network = True

if network:
    product = input("Enter the product: ").strip().lower()
    
    products_lower = [p.lower() for p in products]

    if product in products_lower:
        index = products_lower.index(product)
        
        if stocks[index] == 0:
            print(f'{products[index]} - Out of stock')
        
        elif 1 <= stocks[index] <= 10:
            print(f'{products[index]} - Only few items left. Hurry up!')
        
        else:
            print(f'{products[index]} - Available ({stocks[index]} in stock)')
    
    else:
        print("Product not found")

else:
    print("No Network is found")


students = {
    'ajay': {'python':99, 'mysql':88, 'flask':90},
    'krishna': {'python':29, 'mysql':100, 'flask':50},
    'ruchitha': {'python':98, 'mysql':96, 'flask':99},
    'nishitha': {'python':85, 'mysql':86, 'flask':99},
    'praneetha': {'python':50, 'mysql':70, 'flask':60},
    'satish':{'python':10, 'mysql':20, 'flask':30}
    }

user = input("Enter the User: ")
print(students[user])

avg = (students[user]['python'] + students[user]['mysql'] + students[user]['flask']) / 3

if 80 <= avg <= 100:
    print(f'{[user]} got "A" grade.\nKeep it up')

elif 60 <= avg < 80:
    print(f'{[user]} got "B" grade.\nGood, Need to Inprove')

elif 40 <= avg < 60:
    print(f'{[user]} got "C" grade.\nAverage, Practice well for the next time.')

elif avg <= 40:
    print(f'{[user]} got Failed in exam.\nBring your parents.')

'''
# Output:
Enter the amount: 15000
Amount: 15000
After discount: 7500.0
Enter the budget: 20000
Go for Shopping
Enter a character (a-f): c
Imran will Give Party
******************************
['laptop', 'mouse', 'phone', 'keyboard', 'charger', 'speaker']
******************************
Enter the product: speaker
speaker - Only few items left. Hurry up!
Enter the User: ruchitha
{'python': 98, 'mysql': 96, 'flask': 99}
['ruchitha'] got "A" grade.
Keep it up
'''
