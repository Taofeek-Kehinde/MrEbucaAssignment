"""
PSEUDOCODE:
1. Ask user for a number
2. Convert number to string
3. Set sum = 0
4. For each digit in the string:
   - Convert digit to integer
   - If digit is odd (digit % 2 != 0):
        Add digit to sum
5. Print sum
"""

number = int(input("Enter a number: "))

# Convert to string to loop through digits
num_str = str(number)
odd_sum = 0

for digit_char in num_str:
    digit = int(digit_char)
    if digit % 2 != 0:
        odd_sum = odd_sum + digit

print(f"Sum of odd digits: {odd_sum}")
