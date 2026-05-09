"""
PSEUDOCODE:
1. Ask for weight in kilograms
2. Ask for height in meters
3. Calculate BMI = weight / (height x height)
4. If BMI is less than 18.5:
   - Print "Underweight"
5. If BMI is between 18.5 and 24.9:
   - Print "Normal"
6. If BMI is between 25 and 29.9:
   - Print "Overweight"
7. If BMI is 30 or more:
   - Print "Obese"
"""

weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))


bmi = weight / (height * height)

# Determine category
if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obese"


print(f"Your BMI is: {bmi:.2f}")
print(f"Category: {category}")
