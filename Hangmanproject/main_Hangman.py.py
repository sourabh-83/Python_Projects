import random
# Update the word list to use the world_list from hangman_words.py
# Import the logo from hangman_art.py and print it at the start of the game
from hangman_words import word_list
from hangman_art import stages, logo

# Set lives
lives = 6

# TODO-3: Print the Hangman logo at the start
print(logo)

# Randomly choose a word
chosen_word = random.choice(word_list)
print(f"(The word is: {chosen_word})")  # You can remove this line in production

# Placeholder to track guessed letters
placeholder = "_" * len(chosen_word)
print("Word to guess: " + placeholder)

# Game state tracking
game_over = False
correct_letters = []

while not game_over:
    # TODO-6: Show current number of lives
    print(f"\n*************** {lives}/6 LIVES LEFT ***************")
    guess = input("Enter a letter: ").lower()

    # TODO-4: Inform the user if letter was already guessed
    if guess in correct_letters:
        print(f"You've already guessed '{guess}'. Try a different letter.")
        continue  # Skip the rest and ask for a new letter

    # Add guess to correct_letters (even if it's wrong, to avoid repeating)
    correct_letters.append(guess)

    # Build the display string based on guessed letters
    display = ""
    for letter in chosen_word:
        if letter in correct_letters:
            display += letter
        else:
            display += "_"

    # Show the current word state
    print("Word to guess: " + display)

    # TODO-5: Reduce life if the guess is wrong
    if guess not in chosen_word:
        lives -= 1
        print(f"'{guess}' is not in the word. You lose a life.")
        if lives == 0:
            game_over = True
            print("\nYou lose!")
            print(f"The correct word was: {chosen_word}")
            print(f"*********** IT WAS '{chosen_word.upper()}'! YOU LOST ***********")

    # Check win condition
    if "_" not in display:
        game_over = True
        print("\nYou Win!")
        print(f"*********** CONGRATS! YOU GUESSED '{chosen_word.upper()}' ***********")

    # TODO-7: Show current hangman stage
    print(stages[lives])


