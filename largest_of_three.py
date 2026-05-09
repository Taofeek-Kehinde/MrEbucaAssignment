"""
PSEUDOCODE:
1. Ask for three numbers (a, b, c)
2. Assume largest = a
3. If b is larger than largest:
   - Set largest = b
4. If c is larger than largest:
   - Set largest = c
5. Print largest number
"""

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))


largest = a

if b > largest:
    largest = b

if c > largest:
    largest = c

# Print result
print(f"The largest number is: {largest}")
