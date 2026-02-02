from collections import Counter, defaultdict, deque

s = 'python'
s1 = "Randeer is late to the class Ajay is also late to the class "

print(Counter(s))
print(Counter(s1.split()))

from collections import Counter, defaultdict, deque

s = 'python'
s1 = "Randeer is late to the class Ajay is also late to the class "
l = [1, 2, 3, 4, 2, 1, 3, 4, 5, 12, 23]
t = (1, 2, 3, 4, 2, 1, 3, 4, 5, 12, 23)
set = {1, 2, 3, 4, 2, 1, 3, 4, 5, 12, 23}
print(Counter(s))
print(Counter(s1.split()))
print(Counter(l))
print(Counter(t))
print(Counter(set))

d = {}
s = 'Python Programming'
for i in s:
    if i in d:
        d[i]+= 1
    else:
        d[i]= 1

print(d)

d = defaultdict(int)
s = 'Python Programming'
for i in s:
        d[i]= 1
print(d)

d = deque([])
d.append(10)
d.append(20)
d.append(30)
d.append(40)
d.popleft()
d.popleft()
d.append(80)
d.append(90)

print(d)

q = deque([])
q.appendleft(10)
q.appendleft(20)
q.appendleft(30)
q.appendleft(40)
q.pop()
q.pop()
q.appendleft(80)
q.appendleft(90)

print(q)


from itertools import combinations, permutations

s = 'abc'
print(list(combinations(s,2)))
print(list(permutations(s,2)))
