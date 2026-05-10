"""
PSEUDOCODE:
1. Ask user for a string
2. Set counter = 0
3. For each character in the string:
   - If character is lowercase (a to z):
        Add 1 to counter
4. Print counter
"""

text = input("Enter a string: ")

# Count lowercase letters
count = 0
for char in text:
    if char >= 'a' and char <= 'z':
        count = count + 1

print(f"Number of lowercase letters: {count}")
