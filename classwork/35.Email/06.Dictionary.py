#empty dictionary
d=dict()
d={}
d={'name':'saikrishna','age':'22','address':'Madinaguda'}
print(d['name'])#dict[key] will raise a KeyError if the key does not exist.
print(d.get('name'))#dict.get(key, default_value) will return None or the specified default_value if the key is not found.
d['phno']=124
print(d)
d.pop("age")#Removes the specified key and returns its value.
print(d)
del d['address']
print(d)
d.popitem()#Removes and returns the last inserted key-value pair.
print(d)
d.clear()
print(d)

d={'name':'saikrishna','age':'22','address':'Madinaguda'}
print(d.keys())#Returns a view object containing all keys
print(d.values())#Returns a view object containing all values
print(d.items())#Returns a view object containing all key-value pairs as tuples
print(d.clear())#Removes all key-value pairs, making the dictionary empty

d={'name':'saikrishna','age':'22','address':'Madinaguda'}
del d['name']#Deletes a specific key from the dictionary
print(d)

d={'name':'saikrishna','age':'22','address':'Madinaguda'}
print(len(d))#Returns the number of items in the dictionary
print(max(d))#Returns the maximum key (if keys are comparable)
print(min(d))#Returns the minimum key
print(sorted(d))#Returns sorted list of keys
print(d.setdefault('age',22))#Returns value of key; if key does not exist, inserts it with default value

d={'name':'saikrishna','ph':'22','address':'Madinaguda'}
print(d.setdefault('age',22))
print(d)

#Nested Dictionaries-A dictionary can contain another dictionary as its value.
students = {
    "Alice": {"age": 21, "course": "CS"},
    "Bob": {"age": 22, "course": "Math"}
}
print(students["Alice"]["course"])
