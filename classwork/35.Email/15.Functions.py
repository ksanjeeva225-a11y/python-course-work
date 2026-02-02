def func_name():
    #stmts
    print("This is a function")

func_name()

def wish(name):
    print(f'welcome to codegnan {name}')

wish('Ajay')
wish('Krishna')
wish('Satish')

#Position
def display(username, mail, password):
    print(f'Username: {username}\nMail: {mail}\nPassword: {password}')

uname = input("Enter the username: ")
mail = input("Enter the mail: ")
password = input("Enter the password: ")

display(uname, mail, password)
display(mail, uname, password)
display(password, uname, mail)
display(uname, password, mail)

#Keyword
def display(username, mail, password):
    print(f'Username: {username}\nMail: {mail}\nPassword: {password}')

uname = input("Enter the username: ")
mail = input("Enter the mail: ")
password = input("Enter the password: ")

display(username = uname, mail = mail, password = password)
display(password = password, username = uname, mail = mail)
display(username = uname, password = password, mail = mail)

# Default arguments
def display(username, mail, password='1234'):
    print(f'Username: {username}\nMail: {mail}\nPassword: {password}')

uname = input("Enter the username: ")
mail = input("Enter the mail: ")
password = input("Enter the password: ")

display(uname, mail)
display(uname, mail, password)

#Variable length
def display(*names):
    print(names)

display('Ajay', 'Krishna', 'Ruchitha', 'Varsha', 'Preethi')
display('Santosh', 'Harsha', 'satish')
display('Rama', 'Randeer', 'Priya', 'praveen')
display('Imran', 'Sumanth')
display('Prasad')

#Keyword variable
def squares(**numbers):
    print(numbers)
    
squares(K1 = '1', K2 = '2', K3 = '3')
squares(K1 = '1', K2 = '2')
squares(K1 = '1', K2 = '2', K3 = '3', K4 = '4')
squares(K1 = '1', K2 = '2', K3 = '3', K4 = '4', K5 = '5')

#Scope
name = 'sumanth'

def data(name):
    name = 'ruchitha'
    print("Inside: ", name)

print("Outside: ", name)
data(name)

name='sumanth'
def data():
    global name
    name='ruchitha'
    print("Inside:",name)

data()
print("Outside:",name)

#Non local
def status():
    course = 'Java'
    print("Beg: ", course)
    def change():
        global course
        course='Python'
        print("In bet: ", course)

    change()
    print("Final: ", course)

status()

def status():
    course = 'Java'
    print("Beg: ", course)
    def change():
        nonlocal course
        course='Python'
        print("In bet: ", course)

    change()
    print("Final: ", course)

status()

#Overridden
s = 'codegnan'
length = 16 
print(len(s))
