"""
PSEUDOCODE:
1. Ask user for a string
2. Convert to lowercase (to make case-insensitive)
3. Reverse the string
4. If original equals reversed:
   - Print "Palindrome"
5. Else:
   - Print "Not palindrome"
"""

text = input("Enter a string: ")
text_lower = text.lower()

# Reverse the string
reversed_text = ""
for char in text_lower:
    reversed_text = char + reversed_text

# Check if palindrome
if text_lower == reversed_text:
    print(f"'{text}' is a palindrome")
else:
    print(f"'{text}' is NOT a palindrome")
