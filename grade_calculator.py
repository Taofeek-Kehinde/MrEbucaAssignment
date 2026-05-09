"""
PSEUDOCODE:
1. Get three scores from user
2. Calculate average = (score1 + score2 + score3) / 3
3. Check average against grade ranges:
   - If 90 to 100: grade = 'A'
   - If 80 to 89: grade = 'B'
   - If 70 to 79: grade = 'C'
   - If 60 to 69: grade = 'D'
   - If 0 to 59: grade = 'F'
4. Print the average and letter grade
"""

# Get three scores
score1 = float(input("Enter first score (0-100): "))
score2 = float(input("Enter second score (0-100): "))
score3 = float(input("Enter third score (0-100): "))

# Calculate average
average = (score1 + score2 + score3) / 3

# Determine letter grade
if average >= 90:
    grade = 'A'
elif average >= 80:
    grade = 'B'
elif average >= 70:
    grade = 'C'
elif average >= 60:
    grade = 'D'
else:
    grade = 'F'

# Print results
print(f"Average score: {average:.2f}")
print(f"Letter grade: {grade}")
