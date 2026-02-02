#1. Name Validation
import re

name = input("Enter the name: ")
pattern = r'^[A-Za-z]{2,25}( [A-Za-z]{2,25})+$'
res = bool(re.fullmatch(pattern, name))
print(res)

#2. Email Validation
import re

email = input("Enter the email: ")
pattern = r'^[a-zA_Z0-9.-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
res = bool(re.fullmatch(pattern, email))
print(res)

#3. Phone Number Validation
import re

phonenumber = input("Enter the phonenumber: ")
pattern = r'^(?:\+91|0)?[6-9]\d{9}$'
res = bool(re.fullmatch(pattern, phonenumber))
print(res)

#4. Password Validation
import re

password = input("Enter the password: ")
pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
res = bool(re.fullmatch(pattern, password))
print(res)
