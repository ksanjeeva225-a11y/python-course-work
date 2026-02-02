#Q1.text = "Hello World"
# Convert this string to lowercase and store in result
text = "Hello World"
result = text.lower()
print(result)
#Q2.greeting = "good morning"
# Convert this string to uppercase
greeting = "good morning"
print(greeting.upper())
#Q3.data = " hello python "
# Remove leading and trailing spaces from this string
data = " hello python "
print(data.strip())
#Q4.line = "Python is tough"
# Replace "tough" with "easy"
line = "Python is tough"
print(line.replace("tough", "easy"))
#Q5.word = "banana"
# Count how many times "a" appears in the word
word = "banana"
print(word.count("a"))
#Q6.info = "python is fun"
# Convert this string to a list of words using split
info = "python is fun"
print(info.split())
#Q7.sentence = "learn python"
# Get the length of this string using len()
sentence = "learn python"
print(len(sentence))
#Q8.value = "test123"
# Check if the string is alphanumeric using a string method
value = "test123"
print(value.isalnum())
#Q9.text = "HELLO"
# Convert this string to lowercase and then capitalize the first letter
text = "HELLO"
text.lower()
text.capitalize()
print(text)
#Q10.email = "student@domain.com"
# Check if the string ends with ".com"
email = "student@domain.com"
print(email.endswith(".com"))
#Q11.marks = [45, 67, 89, 32]
# Sort the list in ascending order using sort()
marks = [45, 67, 89, 32]
print(marks.sort())
#Q12.numbers = [10, 20, 30]
# Add 40 to the end of this list
numbers = [10, 20, 30]
numbers.append(40)
print(numbers)
#Q13.colors = ["red", "blue", "green"]
# Remove "blue" from the list
colors = ["red", "blue", "green"]
colors.remove("blue")
print(colors)
#Q14.values = [1, 2, 3, 2, 1]
# Count how many times 2 appears in the list
values = [1, 2, 3, 2, 1]
print(values.count(2))
#Q15.items = ["pen", "book", "pencil"]
# Join the list items into a string separated by commas
items = ["pen", "book", "pencil"]
print(",".join(items))

#Q16.scores = [100, 90, 80]
# Reverse the list using reverse()
scores = [100, 90, 80]
scores.reverse()
print(scores)
#Q17.students = ("Anu", "Ravi", "Meena")
# Get the second item from the tuple and store in a variable
students = ("Anu", "Ravi", "Meena")
second_item = students[1]
print(second_item)
#Q18.details = ("ID101", "Sita", "CSE")
# Convert this tuple to a list
details = ("ID101", "Sita", "CSE")
print(list(details))
#Q19.data = (5, 3, 9, 1)
# Find the maximum value in the tuple
data = (5, 3, 9, 1)
print(max(data))
#Q20.group = ("A", "B", "C", "D")
# Get the last two elements using slicing
group = ("A", "B", "C", "D")
print(group[-2:])
#Q21.names = ["Anu", "Ravi", "Anu", "Sam"]
# Convert the list to a set to remove duplicates
names = ["Anu", "Ravi", "Anu", "Sam"]
print(set(names))
'''
Q22.
a = {1, 2, 3}
b = {2, 3, 4}
'''
# Find the union of sets a and b
a = {1, 2, 3}
b = {2, 3, 4}
print(a.union(b))
'''
Q23.
x = {1, 2, 3}
y = {2, 4}
# Find the intersection of sets x and y
'''
x = {1, 2, 3}
y = {2, 4}
print(x.intersection(y))
#Q24.numbers = {5, 10, 15}
# Add 20 to the set using add()
numbers = {5, 10, 15}
print(numbers.add(20))
#Q25.items = {1, 2, 3, 4}
# Remove 3 from the set using remove()
items = {1, 2, 3, 4}
print(items.remove(3))
#Q26.marks = {"Ravi": 90, "Anu": 85}
# Add a new student "Sita" with 88 marks to the dictionary
marks = {"Ravi": 90, "Anu": 85}
marks["Sita"] = 88
print(marks)
#Q27.student = {"name": "Asha", "grade": "A"}
# Get the value of "grade" using get()
student = {"name": "Asha", "grade": "A"}
print(student.get("grade"))
#Q28.record = {"math": 75, "science": 80}
# Update the value of "math" to 85
record = {"math": 75, "science": 80}
record["math"] = 85
print(record)
#Q29.profile = {"id": 101, "name": "John"}
# Print all keys of the dictionary using keys()
profile = {"id": 101, "name": "John"}
print(profile.keys())
#Q30.data = {"x": 1, "y": 2}
# Remove the key
data = {"x": 1, "y": 2}
print(data.pop("y"))
