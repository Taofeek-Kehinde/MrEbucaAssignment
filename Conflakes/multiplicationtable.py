"""
Read number from user

Loop from 1 to 10

For each index, calculate number * index and print in format n x i = result
"""



number = int(input("Enter a number: "))
for index in range(1, 11):
    print(f"{number} x {index} = {number * index}")
