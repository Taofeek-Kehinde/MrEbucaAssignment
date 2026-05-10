"""
PSEUDOCODE:
1. For number from 2 to 100:
   - Assume number is prime
   - For i from 2 to number-1:
        If number divisible by i:
            Not prime, break
   - If prime, print number
"""

print("Prime numbers between 1 and 100:")

# Check each number from 2 to 100
for num in range(2, 101):
    is_prime = True
    
    # Check if num is prime
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    
    if is_prime:
        print(num, end=" ")
