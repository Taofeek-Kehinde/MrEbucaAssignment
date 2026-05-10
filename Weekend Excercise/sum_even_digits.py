"""
PSEUDOCODE:
1. Ask user for a number
2. Convert number to string
3. Set sum = 0
4. For each digit in the string:
   - Convert digit to integer
   - If digit is even (digit % 2 == 0):
        Add digit to sum
5. Print sum
"""

number = int(input("Enter a number: "))

num_str = str(number)
even_sum = 0

for digit_char in num_str:
    digit = int(digit_char)
    if digit % 2 == 0:
        even_sum = even_sum + digit

# Print result
print(f"Sum of even digits: {even_sum}")
