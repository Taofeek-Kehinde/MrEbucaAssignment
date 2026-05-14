"""
Loop from 5 down to 1 (for start number of each row)

For each row starting at s, loop from s down to 1

Print numbers separated by space
"""

for start in range(5, 0, -1):
    for num in range(start, 0, -1):
        print(num, end=" ")
    print()
