#(Discussion: else Clause) In the script of Fig. 4.1, we did not include an else
#clause in the if...elif statement. What are the possible consequences of this choice?

score = 45
if score >= 90:
    grade = 'A'
elif score >= 70:
    grade = 'B'
else:
    grade = 'F'

print(grade)  # F
