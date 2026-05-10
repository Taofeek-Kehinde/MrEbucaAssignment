"""
PSEUDOCODE:
1. Ask user for a number
2. Convert number to string
3. Reverse the string
4. If original string equals reversed string:
   - Print "Palindrome"
5. Else:
   - Print "Not palindrome"
"""

number = int(input("Enter a number: "))

# Convert to string and reverse
num_str = str(number)
reversed_str = ""
for char in num_str:
    reversed_str = char + reversed_str

# Check if palindrome
if num_str == reversed_str:
    print(f"{number} is a palindrome")
else:
    print(f"{number} is NOT a palindrome")
