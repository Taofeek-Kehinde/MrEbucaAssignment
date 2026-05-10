"""
PSEUDOCODE:
1. Set first = 0, second = 1
2. Print first and second
3. For i from 3 to 20:
   - next = first + second
   - Print next
   - first = second
   - second = next
"""

# First two Fibonacci numbers
a = 0
b = 1

print("First 20 Fibonacci numbers:")
print(a)
print(b)

# Generate next 18 numbers total = 20
for i in range(3, 21):
    c = a + b
    print(c)
    a = b
    b = c
