'''
set-unordered ,mutable collection of unique elements
'''

s=set()#creation of empty set
s1={1,2,3,4,5}
s2={1,2,4,5,6,6,7}
print(s)
print(s1)
print(s2)
'''
proprties of a set

unordered
unique elements
mutable
immutable elements only
'''
boys={'rahul','nikhil','raghu','bittu','gopi','prasad'}
guys={'ramesh','suresh','lokesh','vinay','ajay','arun'}
online={'kittu','prabhu','raghu'}

#1. membership testing
print('rahul' in boys)
print('ramesh' in boys)
print('rahul' not in online)
print("nikhil" not in boys)

#2. union-combining elements from two sets
print(boys | guys)
print(boys.union(guys))

#3. intersection-common elements between two sets.
print(boys & guys)
print(online.intersection(guys))

#4. difference-elements that are in a but not in b
print(guys - online)
print(guys.difference(online))

#5. Symmetric Difference-Returns elements in either set1 or set2 but not both.
print(guys ^ boys)
print(guys.symmetric_difference(boys))

#6. Subset-Checks if all elements of one set are present in another.
print(online <= guys)
print(online.issubset(guys))

#7. superset-Checks if one set contains all elements of another.
print(online >= guys)
print(online.issuperset(guys))

#8. disjoint sets-Returns True if two sets have no common elements.
print(boys.isdisjoint(guys))

#9. Built-in Methods for Sets
a={1,2,3,4,5,5,6,7,8,9}
a.add(10)#Adds an element to the set
print(a)
a.remove(7)#Removes an element; raises an error if the element doesn’t exist
print(a)
a.discard(20)#Removes an element; does not raise an error if the element doesn’t exist
print(a)
a.pop()#Removes and returns an arbitrary element
print(a)
a.clear()#Removes all elements from the set
print(a)

b={1,2,3,4,5,6,7,8}
c={11,22,44,55}
print(b.update(c))#Adds elements from another set to the current set
print(b.intersection_update(c))#Updates the set with the intersection of itself and another set
print(b.difference_update(c))#Updates the set by removing elements found in another set
print(b.symmetric_difference(c))#Updates the set with the symmetric difference

a={1,2,3,4}
b={2,5,6}
print(b.isdisjoint(a))#Returns True if two sets have no elements in common
print(b.issubset(a))#Returns True if the set is a subset of another set
print(b.issuperset(a))#Returns True if the set is a superset of another set
print(len(b))#Returns the number of elements in the set
print(max(b))#Returns the maximum element in the set
print(min(a))#Returns the minimum element in the set
print(sum(a))#Returns the sum of all elements in the set
print(sorted(a))#Returns a sorted list of the set elements

#10. deep copy
a={1,2,3,4}
b={2,5,6}
b=a
b.add(8)
print(b)
print(a)

#11. shallow copy
c=a.copy()
print(a)
c.add(7)
print(c)
print(a)
