"""
PSEUDOCODE:
1. Ask user for a string
2. Create empty string called reversed_string
3. For each character in the original string (from last to first):
   - Add character to reversed_string
4. Print reversed_string
"""

text = input("Enter a string: ")

# Reverse using for loop
reversed_text = ""
for char in text:
    reversed_text = char + reversed_text

print(f"Reversed string: {reversed_text}")
