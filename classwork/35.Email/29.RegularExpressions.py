#1. re.match() – Matches the pattern only at the beginning of the string
import re

s = 'Python programming'
pattern = 'P'
res = re.match(pattern, s)

print(res.group())


#2. re.match() – Checks whether the string starts with an alphanumeric character
import re

s = 'Python programming'
pattern = r'[0-9A-Za-z]'
res = re.match(pattern, s)

print(res.group())


#3. re.match() – Returns None if the pattern does not match at the start
import re

s = '_12ython programming'
pattern = r'[0-9A-Za-z]'
res = re.match(pattern, s)

print(res.group() if res else "Not found")


#4. re.search() – Searches the pattern anywhere in the string
import re

s = 'Python Version 13.0'
pattern = r'\d'
res = re.search(pattern, s)

print(res.group() if res else "Not found")


#5. re.search() – Finds the first occurrence of four consecutive digits
import re

s = '12 3 7896 46923 5678'
pattern = r'\d{4}'
res = re.search(pattern, s)

print(res.group() if res else "Not found")


#6. re.findall() – Returns all two-digit numbers as a list
import re

s = 'cd23 djoejojewoeo cd87 hiehfienhjiaiei ihefioiiorewidwenioifwkp cd12 cd90 cd45'
pattern = r'\d{2}'
res = re.findall(pattern, s)
print(res)


#7. re.finditer() – Returns an iterator with match objects and their positions
import re

s = 'cd23 djoejojewoeo cd87 hiehfienhjiaiei ihefioiiorewidwenioifwkp cd12 cd90 cd45'
pattern = r'\d{2}'
res = re.finditer(pattern, s)

for i in res:
    print(i.start(), i.group())


#8. re.split() – Splits the string wherever the pattern matches
import re

s = 'python,java;c++:javascript#html'
pattern = r'[,;:#]'
res = re.split(pattern, s)
print(res)


#9. re.sub() – Replaces all two-digit numbers with '00'
import re

s = 'vk18, ro45 dh07, bh93, sc10'
res = re.sub(r'[0-9]{2}', '00', s)
print(res)


#10. re.sub() – Replaces all vowels with an asterisk (*)
import re

s = 'vk18, ro45 dh07, bh93, sc10'
res = re.sub(r'[aeiouAEIOU]{1}', '*', s)
print(res)


#11. re.findall() – Finds all substrings matching different dot (.) patterns
import re

s = 'cat cot cut sit rat rod hit hut'
res = re.findall(r'c.t', s)
res1 = re.findall(r'..t', s)
res2 = re.findall(r'.ut', s)
res3 = re.findall(r'r.t', s)

print(res)
print(res1)
print(res2)
print(res3)


#12. re.findall() – Finds uppercase letter at start and lowercase letter at end
import re

s = 'Today is Sumanth"s birthday'
res = re.findall(r'^[A-Z]', s)
res1 = re.findall(r'[a-z]$', s)

print(res)
print(res1)


#13. re.findall() – Demonstrates *, + quantifiers for pattern repetition
import re

s = 'python pyv1 pyvv1 pyvvv1'
res = re.findall(r'py*', s)
res1 = re.findall(r'pyv*', s)
res2 = re.findall(r'pyv+', s)

print(res)
print(res1)
print(res2)


#14. re.findall() – Shows optional (?) and any character (.) matching
import re

s = 'cat ct'
res = re.findall(r'c?t', s)
res1 = re.findall(r'c.t', s)

print(res)
print(res1)


#15. re.findall() – Extracts numbers, lowercase words, and specific groups
import re

s = 'abc23 derabc Sumanth16 Ruchitha19 Randheer45 Ajay18'
res = re.findall(r'[0-9]{2}', s)
res1 = re.findall(r'[a-z]{3}', s)
res2 = re.findall(r'(abc)', s)

print(res)
print(res1)
print(res2)


#16. re.findall() – Uses word boundaries to match whole words only
import re

s = 'cat cat cat cat cat cat cat cat catcat'
res = re.findall(r'\bcat\b', s)
print(res)
