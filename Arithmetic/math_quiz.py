import random

def generate_subtraction_problem():
    num1 = random.randint(5, 20)
    num2 = random.randint(1, 5)
    return (num1, num2, num1 - num2)
