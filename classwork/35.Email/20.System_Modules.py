import sys

print("starting")

#"sys.exit()"
print("ending")

import sys

print(sys.path)

import sys

print(sys.version)

import platform

print(platform.system())
print(platform.release())
print(platform.processor())

import random

#random.seed(10) # Same Output after Excecution
print(random.random())
print(random.randint(1, 10))
print(random.uniform(1, 10))

names = ['krishna', 'nithin', 'sumanth', 'santosh', 'harsha', 'Prasad', 'Ajay']
print(random.choice(names))
print(random.choices(names, k = 3))
print("Before: ", names)
random.shuffle(names)
print("after: ", names)

import math

print(math.pi)
print(math.e)
print(math.sqrt(16))
print(math.pow(2, 5))
print(math.ceil(12.3))
print(math.ceil(12.0000001))
print(math.ceil(12.23))
print(math.ceil(12.83))

print(math.floor(12.9999999999))
print(math.floor(12.3))
print(math.floor(12.83))
print(math.floor(12.9))

print(math.fabs(-12.3))

print(math.factorial(7))

print(math.gcd(50, 100))

print(math.sin(30))
print(math.cos(30))
print(math.tan(30))

print(math.log(2, 2))

print(math.degrees(30))
print(math.radians(12))
