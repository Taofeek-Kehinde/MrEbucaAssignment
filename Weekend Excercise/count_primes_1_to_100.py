"""
PSEUDOCODE:
1. Set counter = 0
2. For number from 2 to 100:
   - Assume number is prime
   - For i from 2 to number-1:
        If number divisible by i:
            Not prime, break
   - If prime, add 1 to counter
3. Print counter
"""

count = 0

for num in range(2, 101):
    is_prime = True
    
    # Check if num is a prime
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    
    if is_prime:
        count = count + 1

# Print result
print(f"Number of prime numbers between 1 and 100: {count}")
