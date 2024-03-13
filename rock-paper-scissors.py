import random

words = ['cat', 'dog', 'wet', 'dry', 'run']

# selecting random word
index = random.randrange(len(words))
word = words[index]

def word_guess(w):
    guess = input("Enter word (3 letters):")

    if guess == w:
        print("Correct guess!")
    else:
        print("Wrong guess, try again.")
        word_guess(w)

word_guess(word);