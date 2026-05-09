"""
PSEUDOCODE:
1. Ask for age
2. If age is less than 5:
   - Price = "Free"
3. If age is between 5 and 12:
   - Price = "$5"
4. If age is between 13 and 64:
   - Price = "$12"
5. If age is 65 or older:
   - Price = "$8"
6. Print price
"""


age = int(input("Enter your age: "))

# Determine ticket price
if age < 5:
    price = "Free"
elif age <= 12:
    price = "$5"
elif age <= 64:
    price = "$12"
else:
    price = "$8"


print(f"Ticket price: {price}")
