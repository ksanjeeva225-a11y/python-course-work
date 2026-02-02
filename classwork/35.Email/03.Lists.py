'''

List Features

Ordered: Lists maintain the order of elements.
Mutable: Elements can be modified after creation.
Indexed: Elements can be accessed using an index (starting from 0).
Allow Duplicates: Lists can contain duplicate values.
Heterogeneous: Lists can contain different data types (e.g., int, str, float, etc.).
Dynamic: Size is not fixed; elements can be added or removed dynamically.

'''
l=[]#empty list
l=list()#empty list using constructor
l=[1,2,3,4,5]
l=list([1,2,3,4,5])
l=[[1,2],[3,4],[5,6]]#nested list
l1=[2,3,4]
l2=[5,6,7]
print(l1+l2)#adding 2 lists
print(l1*3)#multiplying
print(2 in l1)#checking weather 2 is present in l1
print(9 not in l1)#checking weather 9 is not present in l1
l=['ajay','krishna','shekar','santhosh','harsha','varun','shiva']
print(l[2])#indexing
print(l[4])
print(l[-1])
print(l[0:3:1])#slicing
print(l[::-1])
l3=[1,23,44]
l3.append(70)#adding elements to the end
l3.append(80)
l3.append((10,20,30))
print(l3)
l3.append("ruchi")
print(l3)
l3.extend([6,7,8,9])#adds multiple elements
l3.insert(0,20)#adds at a specific position
print(l3)
l3.remove(23)#Removes first occurrence of 23
l3.pop(3)#Removes element at index 3
print(l3)
l3.pop()#removes last element
print(l3)
l3.clear()#Clears the entire list
print(l3)
l5=[2,3,4]
del l5[1]#Deletes element at index 1
print(l5)
l4=[2,3,4,5,6,3,4]
l4.index(5)#Returns the index of the first occurrence of 5.
print(l4)
l4.count(4)#Returns the number of times 4 appears in the list.
print(l4)
l4.sort()#sorts the list
print(l4)
l4.sort(reverse=True)#Sorts the list (ascending by default).
print(l4)
l4.reverse()#Reverses the list in place.
print(l4)
max(l4)#Returns the largest element in the list.
print(l4)
min(l4)#Returns the smallest element in the list.
print(l4)
len(l4)#Returns the number of elements in the list.
print(l4)
'''
Deep copy
'''
a=[1,2,3,4,5]
print(a)
b=a
print(b)
b.append(6)
print(b)
print(a)
'''
Shallow copy
'''
c=a.copy()
print(a)
c.append(7)
print(c)
print(a)
r=[0,0.0,'',[],(),{},set(),False]
print(any(r))
print(all(r))
r=[0,0.0,'',[],(),{},set(),False,2,3]
print(any(r))#Returns True if at least one element is True in the list.
print(all(r))#Returns True if all elements are True in the list.
v=[1,2,3,4,5]
print(any(v))
print(all(v))
