import random

def choose_word():
    words = ["python", "hangman", "programming", "computer", "gpt"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    max_attempts = 6
    guessed_letters = []
    word_to_guess = choose_word()
    attempts = 0

    print("Welcome to Hangman!")
    
    while True:
        print("\nCurrent word: ", display_word(word_to_guess, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if guess.isalpha() and len(guess) == 1:
            if guess in guessed_letters:
                print("You already guessed that letter. Try again.")
                continue

            guessed_letters.append(guess)

            if guess in word_to_guess:
                print("Good guess!")
            else:
                print("Wrong guess!")
                attempts += 1

            if display_word(word_to_guess, guessed_letters) == word_to_guess:
                print("\nCongratulations! You guessed the word:", word_to_guess)
                break

            print("Attempts remaining:", max_attempts - attempts)

            if attempts == max_attempts:
                print("\nSorry, you ran out of attempts. The word was:", word_to_guess)
                break
        else:
            print("Please enter a valid single letter.")

if __name__ == "__main__":
    hangman()
