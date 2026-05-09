"""
PSEUDOCODE:
1. Get first number from user
2. Get operator (+, -, *, /) from user
3. Get second number from user
4. Check which operator was entered:
   - If '+': result = num1 + num2
   - If '-': result = num1 - num2
   - If '*': result = num1 * num2
   - If '/': result = num1 / num2 (if num2 is not 0)
5. Print the result
"""

num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

# Perform calculation
if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Cannot divide by zero."
else:
    result = "Invalid operator!"

# Print result
print(f"{num1} {operator} {num2} = {result}")
