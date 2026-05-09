"""
PSEUDOCODE:
1. Ask for first number (x)
2. Ask for second number (y)
3. If y is not zero:
   - Calculate x divided by y
   - Print the result
4. If y is zero:
   - Print "Cannot divide by zero"
"""

x = int(input("Enter first number (x): "))
y = int(input("Enter second number (y): "))

# Checking if dividing by zero
if y != 0:
    result = x / y
    print(f"{x} / {y} = {result}")
else:
    print("Cannot divide by zero")
