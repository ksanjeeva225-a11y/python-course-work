def wish(name):
    return f"welocome {name}"
print(wish("saikrishna"))
lwish=lambda name : f"welocome {name}"
print(lwish("saikrishna"))

def squares(n):
    return f"square of a num:{n*n}"
print(squares(2))
lsquare=lambda n : f"square of a num:{n*n}" 
print(lsquare(2))

def add(a,b):
    return a+b
print(add(2,3))
ladd= lambda a,b: a+b
print(ladd(2,3))

def area(r):
    return f"area:{3.14*r*r}"
print(area(5))
larea=lambda r:3.14*r*r
#print(larea(5))

def eoro(n):
    if n%2==0:
        print("even")
    else:
        print("odd")
eoro(5)

a="aeiouAEIOU"
ch=input("Enter char")
if ch in a:
    print("vowels")
else:
    print("consonants")
b=lambda ch:"vowels" if ch in a else "consonants"
print(b("e"))

#map
l=[1,2,3,4]
res=list(map(lambda i: f"{i}%",l))
print(res)
names=["saikrishna","satish","Prasad"]
res1=list(map(lambda i: i.title(),names))
print(res1)
price=[2000,30000,4440]
res2=list(map(lambda i: f"{i+i*0.18}%",l))
print(res2)

#filter
l=[1,2,3,4]
res=list(filter(lambda i: i%2==0,l))
print(res)
names=["saikrishna","satish","Prasad"]
res1=list(filter(lambda i: i[0]=="s",names))
print(res1)
price=[2000,30000,4440]
res2=list(filter(lambda i: i>5000,l))
print(res2)

products={
    "milk":0,
    "sugar":30,
    "butter":40,
    "cheese":10
}
res3=list(filter(lambda i: products[i]==0, products))
print(res3)

from functools import reduce
l=[1,2,3,4,5]
res=reduce(lambda a,b: a+b, l)
print(res)

res=reduce(lambda a,b: a*b, l)
print(res)

lang=['java','python','c++']
res=reduce(lambda a,b: a+","+b, lang)
print(res)

d={
   "milk":20,
   "sugar":30,
   "butter":40,
   "cheese":10
}
print(dict(sorted(d.items(),key= lambda i:i[0])))
print(dict(sorted(d.items(),key= lambda i:i[0],reverse=True)))
print(dict(sorted(d.items(),key= lambda i:i[1])))
print(dict(sorted(d.items(),key= lambda i:i[1],reverse=True)))
