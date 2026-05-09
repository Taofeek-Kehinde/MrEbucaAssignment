"""
PSEUDOCODE:
1. Get password input from user
2. Check length of password:
   - If length < 1: strength = "Invalid"
   - If length < 6: strength = "Weak"
   - If length between 6 and 10: strength = "Medium"
   - If length > 10: strength = "Strong"
3. Print password strength
"""


password = input("Enter your password: ")

# Check password length
length = len(password)

# check strength
if length < 1:
    strength = "Invalid"
elif length < 6:
    strength = "Weak"
elif length <= 10:
    strength = "Medium"
else:
    strength = "Strong"

# Printour result
print(f"Password strength: {strength}")
