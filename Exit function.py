import sys  # Required to use sys.exit()

num = int(input("Enter a number: "))

if num < 0:
    print("Error: Negative number entered. Exiting program.")
    sys.exit()  # Exits the program immediately

print("Square of the number is:", num**2)

#OUTPUT
Enter a number: 81 
Square of the number is: 6561

Enter a number: -55
Error: Negative number entered. Exiting program.
