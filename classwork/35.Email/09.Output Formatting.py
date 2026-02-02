'''
Output formatting
'''

#basic printing a text:
print("hello.World!")  # hello.World!

#printing multiple items:
name = "Saikrishna"
batch = "PFS-41"
print("name: ", name, "batch: ", batch)  # name: Saikrishna batch: PFS-41

#using sep:
print("2025", "01", "30", sep="-")  # 2025-01-30

#using end:
print("hello", "python", end=" ")  # hello python

#new line:
print("line1\nline2")  # it prints in new line

# \tab: it provides 4 spaces:
print("hello\t,world")  # hello    ,world

#output formatting methods:
name = "Saikrishna"
age = 22
cgpa = 7.67

#1. comma-separated:
print("name: ", name, "Age: ", age, "cgpa: ", cgpa)
# output: name: Saikrishna Age: 22 cgpa: 7.67

#2. using modulo operator:
print("name:%s | Age:%d | cgpa: %f" % (name, age, cgpa))
# output: name:Saikrishna | Age:22 | cgpa: 7.670000

#3. f-strings:
print(f"name:{name} age:{age} cgpa:{cgpa}")
# output: name:Saikrishna age:22 cgpa:7.67
#4. str.format() method:
print("Name: {} Age: {} cgpa: {}".format(name, age, cgpa))
# output: Name: Saikrishna Age: 22 cgpa: 7.67
