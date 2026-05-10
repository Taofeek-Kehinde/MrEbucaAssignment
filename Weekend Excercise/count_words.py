"""
PSEUDOCODE:
1. Ask user for a sentence
2. Split the sentence by spaces
3. Count how many parts we get
4. Print the count
"""

sentence = input("Enter a sentence: ")

# Count words by splitting on spaces
words = sentence.split()
word_count = len(words)

print(f"Number of words: {word_count}")
