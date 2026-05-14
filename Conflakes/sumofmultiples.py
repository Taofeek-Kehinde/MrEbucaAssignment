"""
Initialize total = 0

Loop from 10 to 20,000 in steps of 10

Add each number to total

Print total
"""

total = 0
for num in range(10, 20001, 10):
    total += num
print("Sum of multiples of 10 between 1 and 20000:", total)
