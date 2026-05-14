import unittest
from math_quiz import generate_subtraction_problem

class TestMathQuiz(unittest.TestCase):
    
    def test_returns_three_numbers(self):
        result = generate_subtraction_problem()
        self.assertEqual(len(result), 3)

    def test_first_number_big_or_equal(self):
        num1, num2, answer = generate_subtraction_problem()
        self.assertTrue(num1 >= num2)

    def test_numbers_change(self):
        first = generate_subtraction_problem()
        second = generate_subtraction_problem()
        self.assertNotEqual(first, second)
