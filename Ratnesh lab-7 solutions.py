#Taking input from the user
number = int(input("Enter a number: "))
result = "Even" if number % 2 == 0 else "Odd"
print(f"The number {number} is {result}.")

# Taking two numbers as input from the user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num1, num2 = num2, num1
print(f"After swapping: First number = {num1}, Second number = {num2}")

# Taking kilometers as input from the user
kilometers = float(input("Enter distance in kilometers: "))
miles = kilometers * 0.621371
print(f"{kilometers} kilometers is equal to {miles} miles.")

# Given values
P = 200  
R = 5    
T = 5    
SI = (P * R * T) / 100
print(f"The Simple Interest on Rs. {P} for {T} years at {R}% per year is Rs. {SI}.")