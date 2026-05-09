"""
PSEUDOCODE (Super Simple):
1. Ask for a year
2. Check if year can be divided by 4:
   - If yes, it's a leap year
   - UNLESS it can be divided by 100:
        Then it's NOT a leap year
        EXCEPT if it can be divided by 400:
            Then it IS a leap year
3. Tell the user the answer
"""


# Get the year from user 
year = int(input("Enter a year: "))


if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(f"{year} is a leap year!")
else:
    print(f"{year} is NOT a leap year.")
