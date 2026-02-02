'''
Tuple-
'''
#Tuple creation
T=()#empty tuple
t=tuple()#empty tuple using constuctor
t1=(1,2,3,4,5,6)#multi-element
t2=tuple((1,2,3,4))
print(T)
print(t)
print(t1)
print(t2)
t=(1,)#declaring a single element
print(t)
t=1,2,3,4,5,6,7,8
print(t)
t=('int','float','bool','string','set')
print(t[0])
print(t[-1])
#slicing-[start:end+1:step]
print(t[::1])
print(t[::-1])
print(t[::2])
print(t[::3])
print(t[2::])
#operations on tuple
t1=(1,2,3)
t2=(4,5,6)
print(t1+t2)#concatination
print(t1*3)#repitation
#membership operation
print(3 in t1)
print(5 in t2)
print(2 in t2)
print(3 not in t1)
print(4 not in t2)
t1=(1,2,3,4,5,2,3,4,5)
#count the number of times the element is present
print(t1.count(2))
print(t1.count(1))
#return the index of element
print(t1.index(3))
print(t1.index(5))
#length of the tuple
print(len(t1))
#maximum element
print(max(t1))
#minimum element
print(min(t1))
#total sum of elements
print(sum(t1))
t1=('Sai Krishna','Prasad','Mohan')
print(min(t1))#minimum string in a tuple
print(max(t1))#maximum string in a tuple
