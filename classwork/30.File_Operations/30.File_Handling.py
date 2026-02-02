#1 Opening a file in read mode
file = open('class.txt','r')
print(file.read())

#2 Reading a file line by line
try:
    file = open('class.txt', 'r')
except FileNotFoundError:
    print("File is not present")
else:
    print(file.read())
    file.seek(0)
    print(file.readline())
    file.seek(0)
    print(file.readlines())
    file.close()

#3 Using 'with' statement to handle files
try:
    with open('class.txt', 'r') as file:
        print(file.read())
        file.seek(0)
        print(file.readline())
        file.seek(0)
        print(file.readlines())
        
except FileNotFoundError:
    print("File is not present")

#4 Writing and appending to a file
with open('class.txt', 'w') as file:
    file.write("File Operations")

#5 Appending to a file
with open('class.txt', 'a') as file:
    file.write("Exception Handling")

#6 Using different modes to read and write
with open('class.txt', 'a+') as file:
    file.write("\nException Handling..........")
    file.seek(0)
    print(file.read())

#7 Using 'w+' and 'r+' modes
with open('class.txt', 'w+') as file:
    file.write("\nException Handling..........")
    file.seek(0)
    print(file.read())

with open('class.txt', 'r+') as file:
    file.write("\nException Handling..........")
    file.seek(0)
    print(file.read())
