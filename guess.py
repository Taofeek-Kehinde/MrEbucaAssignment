#(Guess the Number) Write a script that plays “guess the number.” Choose the
#number to be guessed by selecting a random integer in the range 1 to 1000. Do not reveal
#this number to the user. Display the prompt "Guess my number between 1 and 1000 with
#the fewest guesses:". The player inputs a first guess. If the guess is incorrect, display
#"Too high. Try again." or "Too low. Try again." as appropriate to help the player “zero
#in” on the correct answer, then prompt the user for the next guess. When the user enters
#the correct answer, display "Congratulations. You guessed the number!", and allow the
#user to choose whether to play again.

import random

while True:  
    secret = random.randint(1, 1000)  
    guesses = 0
    
    print("Guess my number between 1 and 1000 with the fewest guesses:")
    
    while True:  
        guess = int(input("Enter your guess: "))
        guesses += 1
        
        if guess == secret:
            print("Congratulations. You guessed the number!")
            print(f"It took you {guesses} guesses.")
            break
        elif guess > secret:
            print("Too high. Try again.")
        else:  
            print("Too low. Try again.")
    
    # Ask if user wants to play again
    play_again = input("Play again? (y/n): ")
    if play_again.lower() != 'y':
        print("Thanks for playing!")
        break
