"""
PSEUDOCODE:
1. Get father's age from user (1-80)
2. Get son's age from user (1-80)
3. Calculate age difference = father_age - son_age
4. Find years ago/future when father was/is twice as old:
   - Father's age = 2 * son's age
   - Let x = years ago (negative if in future)
   - (father_age + x) = 2 * (son_age + x)
   - father_age + x = 2*son_age + 2x
   - father_age - 2*son_age = x
   - x = father_age - 2*son_age
5. If x is negative, father will be twice as old in x years
   If x is positive, father was twice as old x years ago
6. Print absolute value of x
"""

father_age = int(input("Enter father's age (1-80): "))
son_age = int(input("Enter son's age (1-80): "))


years = father_age - (2 * son_age)

if years < 0:
    years = -years


print(f"The father will be/was twice as old as his son in {years} years.")
