#1. Basic try-except
try:
    a = 10 / 0
    
except ZeroDivisionError:
    print("You can't divide a number with zero")
    
else:
    print("You have divided successfully")

finally:
    print("End of the try block")
    
print("rest of the code")

#2. Multiple except blocks
try:
    a = b / 10
    a = int([1, 2, 3])
except ZeroDivisionError:
    print("You can't divide a number with zero")
    
except NameError:
    print("You didn't define the variable")
    
except TypeError:
    print("You can change this data type into other one")
else:
    print("You have divided successfully")

finally:
    print("End of the try block")
    
print("rest of the code")

#3. Single except block for multiple exceptions
try:
    a = int([1, 2, 3])
    
except (ZeroDivisionError, NameError, TypeError, KeyError, IndexError) as e:
    print("Error Occured:", e)

else:
    print("You have divided successfully")

finally:
    print("End of the try block")
    
print("rest of the code")

#4. Using Exception class
try:
    a = a + ([1, 2, 3])
    
except Exception as e:
    print("Error Occured:", e)

else:
    print("You have divided successfully")

finally:
    print("End of the try block")
    
print("rest of the code")

#5. Raising an exception
try:
    a = int(input("Enter the number: "))
    if a < 0:
        raise Exception("Negative number not allowed")
    
except Exception as e:
    print("Error Occured:", e)

else:
    print("You have divided successfully")

finally:
    print("End of the try block")
    
print("rest of the code")

#6. Nested try-except blocks
try:
    a = int(input("Enter the number: "))
    try:
        a = b / 10
    except Exception as e:
        print("Error Occured:", e)
    
except Exception as e:
    print("Error Occured:", e)

else:
    print("You have divided successfully")

finally:
    print("End of the try block")
    
print("rest of the code")
