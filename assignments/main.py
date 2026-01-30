import my_programs as mp

while True:
    print("\n====== PYTHON FUNCTION BANK ======")
    print("1. Sum of Two Numbers")
    print("2. Even or Odd")
    print("3. Factorial")
    print("4. Prime Number Check")
    print("5. Reverse String")
    print("6. Palindrome Check")
    print("7. Count Vowels")
    print("8. Largest of Three Numbers")
    print("9. Sum of Digits")
    print("10. Fibonacci Series")
    print("11. GCD of Two Numbers")
    print("12. LCM of Two Numbers")
    print("13. Decimal to Binary")
    print("14. Count Words in String")
    print("15. Multiplication Table")
    print("16. Leap Year Check")
    print("17. Power of a Number")
    print("18. Area of Circle")
    print("19. Simple Interest")
    print("20. Celsius to Fahrenheit")
    print("0. Exit")
    print("=================================")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        mp.sum_two_numbers()
    elif choice == 2:
        mp.even_odd()
    elif choice == 3:
        mp.factorial()
    elif choice == 4:
        mp.prime_check()
    elif choice == 5:
        mp.reverse_string()
    elif choice == 6:
        mp.palindrome()
    elif choice == 7:
        mp.count_vowels()
    elif choice == 8:
        mp.largest_of_three()
    elif choice == 9:
        mp.sum_of_digits()
    elif choice == 10:
        mp.fibonacci()
    elif choice == 11:
        mp.gcd()
    elif choice == 12:
        mp.lcm()
    elif choice == 13:
        mp.decimal_to_binary()
    elif choice == 14:
        mp.count_words()
    elif choice == 15:
        mp.multiplication_table()
    elif choice == 16:
        mp.leap_year()
    elif choice == 17:
        mp.power()
    elif choice == 18:
        mp.area_circle()
    elif choice == 19:
        mp.simple_interest()
    elif choice == 20:
        mp.temperature_conversion()
    elif choice == 0:
        print("Exiting Function Bank. Thank you!")
        break
    else:
        print("Invalid choice! Please try again.")