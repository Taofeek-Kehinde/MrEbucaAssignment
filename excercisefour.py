#(What’s Does This Code Do?) What does the following mystery function do? Assume you pass the list [1, 2, 3, 4, 5] as an argument.

def mystery(x):
    y = 0
    for value in x:
        y += value ** 2   # y = y + value squared
    return y

print(mystery([1, 2, 3, 4, 5]))

#It calculates the sum of squares.
