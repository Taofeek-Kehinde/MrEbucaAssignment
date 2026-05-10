"""
PSEUDOCODE:
1. Ask user for a string
2. Set counter = 0
3. For each character in the string:
   - If character is uppercase (A to Z):
        Add 1 to counter
4. Print counter
"""

text = input("Enter a string: ")

# Count uppercase letters
count = 0
for char in text:
    if char >= 'A' and char <= 'Z':
        count = count + 1

print(f"Number of uppercase letters: {count}")
