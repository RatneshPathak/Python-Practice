#Program in Python to accept two number from the user and calculate their square.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
square_num1 = num1 ** 2
square_num2 = num2 ** 2
print(f"The square of {num1} is {square_num1}.")
print(f"The square of {num2} is {square_num2}.")

#Python Program to check if a number is even or odd
number = int(input("Enter a number: "))
result = "Even" if number % 2 == 0 else "Odd"
print(f"The number {number} is {result}.")