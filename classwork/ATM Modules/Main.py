import ATM

ATM.check_balance()
ATM.deposit_money()
ATM.withdraw_money()
ATM.show_transactions()
'''
--------------------------
import ATM as a
a.check_balance()
a.deposit_money()
a.withdraw_money()
a.show_transactions()
--------------------------
from ATM import check_balance, deposit_money
check_balance()
deposit_money()
--------------------------
from ATM import *
check_balance()
deposit_money()
withdraw_money()
show_transactions()
'''

account_number = input("Enter the account_number: ")
pin = input("Enter the pin: ")

# Login using ATM.login()
if ATM.login(account_number, int(pin)):
    while True:
        ATM.display_menu()
        ch = int(input("Enter the choice: "))
        
        if ch == 1:
            ATM.check_balance()
        elif ch == 2:
            ATM.deposit_money()
        elif ch == 3:
            ATM.withdraw_money()
        elif ch == 4:
            ATM.show_transactions()
        elif ch == 5:
            ATM.change_pin()
        elif ch == 6:
            print("Thankyou, Bye!!!!")
            break
        else:
            print("Enter the valid choice")
else:
    print("Login Failed!")
