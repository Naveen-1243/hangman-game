import random

words = ["python", "javascript", "developer", "programming", "hangman", "computer"]

def play_hangman():

    word = random.choice(words)
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect_guesses = 6  
    revealed_word = ["_" for _ in word]  

    print("Welcome to Hangman!")
    print("Guess the word:", " ".join(revealed_word))
    print(f"You have {max_incorrect_guesses} incorrect guesses allowed.\n")
    
    while incorrect_guesses < max_incorrect_guesses and "_" in revealed_word:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
            for i, letter in enumerate(word):
                if letter == guess:
                    revealed_word[i] = guess
        else:
            incorrect_guesses += 1
            print(f"Sorry, '{guess}' is not in the word. Incorrect guesses: {incorrect_guesses}")

        print("Word:", " ".join(revealed_word))
        print("Guessed letters:", ", ".join(guessed_letters))

    if "_" not in revealed_word:
        print("\nCongratulations! You've guessed the word:", word)
    else:
        print("\nGame Over! The word was:", word)

play_hangman()