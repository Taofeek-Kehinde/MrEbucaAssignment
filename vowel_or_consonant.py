"""
PSEUDOCODE:
1. Ask for one letter
2. Convert letter to lowercase (to handle uppercase inputs)
3. If letter is a, e, i, o, or u:
   - Print "Vowel"
4. Else if letter is a letter (a to z):
   - Print "Consonant"
5. Else:
   - Print "Invalid input"
"""

letter = input("Enter one letter: ")

letter = letter.lower()

# Check if it's a letter (length should be 1 and alphabetic)
if len(letter) == 1 and letter.isalpha():

    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Invalid input")
