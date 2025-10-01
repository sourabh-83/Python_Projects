import random

# Hangman stages art (when lives go down)
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
      |
      |
      |
      |
=========''']

# Word list to choose from
word_list = ["sourab", "aman", "ankit", "sanjana"]

# Choose a word randomly
chosen_word = random.choice(word_list)
print(f"( The word is: {chosen_word}")  # Optional: show for testing

# TODO-1: Set lives to 6 (maximum attempts)
lives = 6

# Create the placeholder (e.g., "______" for "sourab")
placeholder = ""
word_length = len(chosen_word)
for _ in range(word_length):
    placeholder += "_"
print(placeholder)

# Variables to track game state
game_over = False
correct_letters = []

# Main game loop
while not game_over:
    guess = input("Enter a letter: ").lower()
    display = ""

    # Update display with correct guesses
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    # TODO-2: Reduce lives if guess is wrong
    # If guests is not a letter in the chosen_word, Then reduce lives by 1. 
    # If lives goes down tom0 then the game should end, and it should print "you lose".
    if guess not in chosen_word:
        lives -= 1
        print(f"Wrong guess. You have {lives} lives left.")
        if lives == 0:
            game_over = True
            print("You lose!")
            print(f"The word was: {chosen_word}")

    # Win condition
    if "_" not in display:
        game_over = True
        print("You Win!")

    # TODO-3: Print current hangman stage
    # If guests is not a letter in the chosen_word, Then reduce lives by 1. 
    # If lives goes down tom0 then the game should end, and it should print "you lose".
    print(stages[lives])
