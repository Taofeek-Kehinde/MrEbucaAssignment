from math_quiz import generate_subtraction_problem

def ask_question(num1, num2):
    for attempt in range(2):
        user_answer = int(input(f"What is {num1} - {num2}? "))
        if user_answer == (num1 - num2):
            print("Correct!")
            return True
        else:
            print("Wrong! Try again Later.")
    print(f"Out of attempts! The answer was {num1 - num2}")
    return False

def run_quiz():
    score = 0
    print("=" * 40)
    print("MATH QUIZ")
    print("=" * 40)
    
    for question_num in range(1, 11):
        print(f"\nQuestion {question_num}/10")
        num1, num2, answer = generate_subtraction_problem() 
        
        if ask_question(num1, num2):
            score = score + 1
        
        print(f"Score: {score}/10")
    
    return score

run_quiz()
