"""
PSEUDOCODE:
1. Ask user for an integer
2. Convert to string
3. Reverse the string using for loop
4. Convert back to integer
5. Print reversed number
"""
t
number = int(input("Enter an integer: "))

# Convert to string and reverse
num_str = str(number)
reversed_str = ""
for char in num_str:
    reversed_str = char + reversed_str

# Convert back to integer
reversed_num = int(reversed_str)

print(f"Reversed number: {reversed_num}")
