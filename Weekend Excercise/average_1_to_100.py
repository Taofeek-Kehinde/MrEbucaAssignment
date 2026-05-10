"""
PSEUDOCODE:
1. Set sum = 0
2. For number from 1 to 100:
   - Add number to sum
3. Calculate average = sum / 100
4. Print average
"""

total_sum = 0
for num in range(1, 101):
    total_sum = total_sum + num


average = total_sum / 100

print(f"Average of numbers 1 to 100: {average}")
