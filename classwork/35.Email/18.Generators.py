def reels(data):
    for i in data:
        yield i

data=['1..100', '100..200', '200..300', '300..400', '400..500', '500..600']
scroll = reels(data)

while True:
    ch = input("[S]croll or [B]ack: ").lower()
    if ch == 's':
        print(next(scroll))
    else:
        print("Exit")
        break


def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1
        
counter = count_up_to(5)
print(next(counter)) # Output: 1
print(next(counter)) # Output: 2

def square_numbers(n):
    for i in range(n):
        yield i * i
        
squares = square_numbers(5)
print(next(squares)) # Output: 0
print(next(squares)) # Output: 1

#yield Keyword
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1
        
counter = count_up_to(3)
print(next(counter)) # Output: 1
print(next(counter)) # Output: 2
print(next(counter)) # Output: 3
print(next(counter)) # Raises StopIteration

#next Function
def countdown(n):
    while n > 0:
        yield n
        n -= 1
        
cd = countdown(3)
print(next(cd)) # Output: 3
print(next(cd)) # Output: 2
print(next(cd)) # Output: 1
print(next(cd)) # Raises StopIteration
