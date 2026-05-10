"""
PSEUDOCODE:
1. Ask user for a string
2. For each character in the string:
   - Get ASCII value using ord()
   - Print character and its ASCII value
"""

# Get input
text = input("Enter a string: ")

# Print each character with ASCII value
for char in text:
    ascii_value = ord(char)
    print(f"'{char}' = {ascii_value}")
