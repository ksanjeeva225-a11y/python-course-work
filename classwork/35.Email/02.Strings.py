'''
string operations
'''
#1. String Concatenation - Joining 2 or more strings
s1='Sai Krishna' 
s2='Iyer'
print("s1 + s2:",s1 + s2)
print("s1 +' '+ s2:",s1 +' '+ s2)

#2. String Repetition - Repeating a string multiple times
print("s1 * 10:",s1 * 10)
print('*'*10)
print('r'*10)

#3. Indexing - Accessing individual characters using indices
'''
S a i   K r i s h n a
0 1 2 3 4 5 6 7 8 9 10 - Positive Indexing
-11 -10 ...           - Negative Indexing
'''
print("s1[3]:",s1[3]) # output-s1[3]: (space, the 4th character)
print("s1[-1]:",s1[-1]) # output-s1[-1]: a (last character)

#4. Slicing - Extracting a part of the string
names="SaikrishnaGovardhanPrasad" # (This string remains the original value)
# syntax=string_name[start : end+1 : step]

print("names[0:10:1]:",names[0:10:1]) #names[0:10:1]: Saikrishna
print("names[10:19:1]:",names[10:19:1]) #names[10:19:1]: Govardhan
print("names[19:25:1]:",names[19:25:1]) #names[19:25:1]: Prasad
print("names[19::1]:",names[19::1]) #names[19::1]: Prasad
print("names[-6::1]:",names[-6::1]) #names[-6::1]: Prasad
print("names[-15:-6:1]:",names[-15:-6:1])#names[-15:-6:1]: Govardhan
print("names[-15::1]:",names[-15::1]) #names[-15::1]: GovardhanPrasad
print("names[:-15:1]:",names[:-15:1])#names[:-15:1]: Saikrishna
print("names[::-1]:",names[::-1]) #names[::-1]: dasarPnahdravoGanhsirkiaS

#5. Membership operation
print('Saikrishna' in names) #True
print('Sai' in names) #True
print('Govardhan' in names) #True
print('Prasad' not in names) #False
print('Gopal' in names) #False

#6. Case Conversion Methods
print(names.upper()) # Converts all characters to uppercase. SAIKRISHNAGOVARDHANPRASAD
print(names.lower()) # Converts all characters to lowercase. saikrishnagovardhanprasad
print(names.title()) # Capitalizes the first character. Saikrishnagovardhanprasad
print(names.capitalize()) # Capitalizes the first letter of each word. Saikrishnagovardhanprasad
print(names.swapcase()) # Swaps case: upper → lower, lower -> upper. sAIKRISHNAgOVARDHANpRASAD
print(names.casefold()) # Converts to lowercase (more aggressive than lower()). saikrishnagovardhanprasad

#7. Alignment & Formatting Methods
print(s1.center(100,'*')) #Centers the string within width. -> ********************************************Sai Krishna*********************************************
print(s1.center(100,'-')) # --------------------------------------------Sai Krishna--------------------------------------------- 
print(s1.ljust(100,'*')) #Left-aligns the string within width. ->Sai Krishna*****************************************************************************************
print(s1.rjust(100,'*')) #Right-aligns the string within width.-> *****************************************************************************************Sai Krishna
print(s1.zfill(12)) #Pads the string with zeros on the left. -> 0Sai Krishna
print(s1.format())#formats strings dynamically.
n="SaiKrishnaIyer" 

#8. Search & Find Methods
print(n.find('u')) #Returns the index of first occurrence, -1 if not found. -> -1
print(n.find('S')) # MODIFIED: Changed 'R' to 'S' 0
print(n.rfind('a')) #Returns the last occurrence of the substring. ->9
print(n.count('i')) # MODIFIED: Changed 'u' to 'i'
print(n.index('h')) #Like find(), but raises an error if not found. ->7
print(n.rindex('r')) #Like rfind(), but raises an error if not found. ->13

#9. Replace & Modify Methods
print(n.replace('h','*'))#Replaces occurrences of old with new. SaiKris*naIyer
print(n.replace('a','-')) #S-iKrishn-Iyer
print(n.maketrans('hra','***'))#Creates a translation table for translate(). S*iK*is*n*Iye*
print(n.translate(n.maketrans('hra','***')))#Replaces characters using a translation table. {104: 42, 114: 42, 97: 42}

#10. Splitting & Joining methods
v="python programing"
print(v.split())
print(v.split('o'))
v="python,programing,lang"
print(v.split(','))
print(v.rsplit(',',1))
print(v.splitlines())
print(v.join("-")) # Note: This line uses 'v' to join '-', not the other way around. The output format in the original code is misleading.
print(v.partition("."))
print(v.rpartition("-"))

#11. Whitespace & Trimming Methods
print(v.strip())#To remove white spaces
print(v.rstrip())#To remove rightside white spaces
print(v.lstrip())#To remove leftside white spaces

#12. Encoding & Decoding Methods
'''
encode-converting string into bytes
devode-converting bytes into string
'''
u='hello'

#13. String Testing Methods
print(u.startswith('h'))#True
print(u.endswith('o')) #True
print(u.isalpha())#True
print(u.isalnum())#True
print(u.islower())#True
print(u.isupper())#False
print(u.isspace())#False
print(u.istitle())#False
print(u.isidentifier())#True
# len() - Returns the length of the string.
print(len(u))#5
# max() - Returns the maximum
print(max(u))#o
# min() - Returns the minimum
print(min(u))#e
# sorted() - Returns a sorted list of characters.
print(sorted(u))#['e', 'h', 'l', 'l', 'o']
# chr() / ord() - Converts between characters and their ASCII codes.
print(chr(97))#a
print(ord("a"))#97
print('123'.isdecimal()) #True
print('123'.isdigit()) #True
print('12.3'.isdigit()) # False
print('abc'.isnumeric()) #False
