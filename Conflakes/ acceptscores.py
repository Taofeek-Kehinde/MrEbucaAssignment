"""
Set pass_mark = 45, pass_count = 0, fail_count = 0

Loop 15 times:

Ask user for score

If score >= pass_mark, increment pass_count else increment fail_count

Print number of students who passed and failed
"""

pass_mark = 45
pass_count = 0
fail_count = 0

for i in range(1, 16):
    score = float(input(f"Enter score for student {i}: "))
    if score >= pass_mark:
        pass_count += 1
    else:
        fail_count += 1

print(f"Number of students who passed: {pass_count}")
print(f"Number of students who failed: {fail_count}")
