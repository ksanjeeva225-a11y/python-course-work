# ATM Machine
username = 'username'
global pin
pin = 1234
data = {'balance': 22000, 'history': []}

def Login():
    euname = input("Enter the username: ")
    epin = int(input("Enter the pin: "))
    if euname == username and pin == epin:
        print("Login was Successful")
    else:
        print("Login was unsuccessful. Please try again!!")

def Withdraw():
    amount = int(input("Enter the amount to withdraw: "))
    if data['balance'] >= amount:
        data['balance'] -= amount
        print(f'{amount} is withdrawn')
        data['history'].append(f'{amount} is withdrawn')
    else:
        print("Insufficient Balance")

def Deposit():
    amount = int(input("Enter the amount to deposit: "))
    data['balance'] += amount
    print(f'{amount} is deposited')
    data['history'].append(f'{amount} is deposited')

def Check_Balance():
    print(f"Current Balance: {data['balance']}")

def View_Transactions():
    if data['history']:
        print("Transaction History: ".center(40, '-'))
        for transaction in data['history']:
            print(transaction)
        print("End of History".center(40, '-'))
    else:
        print("No Transactions yet")

def Change_pin():
    global pin  # To modify the global pin variable
    epin = int(input("Enter the old pin: "))
    if epin == pin:
        new_pin = int(input("Enter the new pin: "))
        pin = new_pin
        print("Pin changed successfully")
    else:
        print("Incorrect old pin. Please try again!!")

def Exit():
    print("Thanks for using the ATM!")

print("Welcome to ATM".center(30, '='))

while True:
    print("1. Login")
    print("2. Withdraw")
    print("3. Deposit")
    print("4. Check Balance")
    print("5. View Transactions")
    print("6. Change Pin")
    print("7. Exit")

    ch = int(input("Enter the choice: "))
    if ch == 1:
        Login()
    elif ch == 2:
        Withdraw()
    elif ch == 3:
        Deposit()
    elif ch == 4:
        Check_Balance()
    elif ch == 5:
        View_Transactions()
    elif ch == 6:
        Change_pin()
    elif ch == 7:
        Exit()
        break
    else:
        print("Invalid Choice. Please try again!!")
