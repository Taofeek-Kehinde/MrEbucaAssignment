"""
PSEUDOCODE:
1. Ask for x coordinate
2. Ask for y coordinate
3. If x is zero AND y is zero:
   - Print "Origin"
4. If y is zero AND x is not zero:
   - Print "X-axis"
5. If x is zero AND y is not zero:
   - Print "Y-axis"
6. If x is positive AND y is positive:
   - Print "Q1"
7. If x is negative AND y is positive:
   - Print "Q2"
8. If x is negative AND y is negative:
   - Print "Q3"
9. If x is positive AND y is negative:
   - Print "Q4"
"""

x = int(input("Enter x coordinate: "))
y = int(input("Enter y coordinate: "))

if x == 0 and y == 0:
    print("Origin")
elif y == 0 and x != 0:
    print("X-axis")
elif x == 0 and y != 0:
    print("Y-axis")
elif x > 0 and y > 0:
    print("Q1")
elif x < 0 and y > 0:
    print("Q2")
elif x < 0 and y < 0:
    print("Q3")
elif x > 0 and y < 0:
    print("Q4")
