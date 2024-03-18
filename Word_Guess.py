
#Programmer: Timi Ndubuisi-Edeh
#Program Name: Word_Guess v1.0


import random

# Greet the player and ask for their name
print("Word_Guess v1.0")
name = input("May I know your name? ")

# List of possible words to guess
guess_list = ["apple", "orange", "mango", "banana", "lemons"]


# Main function to start the game
def play():
    # Welcome the player and explain the rules
    print(f"Hello {name}!!")
    print(f"{name}, you have only two attempts to guess each word letter")

    # Randomly select a word from the list
    rand_word = random.choice(guess_list)
    # Initialize the number of attempts
    max_attempt = 0

    # Create a placeholder for the word to display guessed letters
    placehold_word = ["_"] * len(rand_word)
    # Keep track of guessed letters to prevent repetition
    guess_letters = []

    # Main game loop; runs until the player runs out of attempts
    while max_attempt < 2:
        # Show the current state of the word
        print(f"Current word is {' '.join(placehold_word)}")
        # Ask the player to guess a letter
        letter = input("Guess a letter: ").lower()

        # Check if the letter was already guessed
        if letter in guess_letters:
            print(f"Sorry, you need to guess a different a different letter")
            continue
        else:
            # If not, add it to the list of guessed letters
            guess_letters.append(letter)

        # Check if the guessed letter is in the word
        if letter in rand_word:
            # Update the placeholder with the correctly guessed letter
            for index, char in enumerate(rand_word):
                if letter == char:
                    placehold_word[index] = letter
            print(f"Good job, you guessed the letter right")

            # If there are no more blanks, the player has guessed the word
            if "_" not in placehold_word:
                print(f"Congratulations! You guessed the word: {rand_word}")
                break
        else:
            # If the letter is not in the word, inform the player and increment the attempt counter
            print(f"Sorry {name}, you guessed wrong, try again")
            max_attempt += 1

        # If the player has used all attempts without guessing the word
        if max_attempt == 2:
            print(f"You've used all attempts. The word was: {rand_word}")

    # Ask the player if they want to play again
    replay = input("Do you want to play again. Y/N: ").lower()
    # Handle the player's response
    if replay == "y":
        play()  # Restart the game
    elif replay != "n":
        print("Your answer needs to be Y for Yes and N for No")  # Handle invalid input
    else:
        print("Thanks for playing")  # End the game


# Start the game
play()
