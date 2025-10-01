import random 
# program1: Pincking a Random Words and Chaecking
'''word_list= ["Sourab","Aman","Ankit"]
# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print in it.
chosen_word = random.choice(word_list) 
print(chosen_word)

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. make guess lowercase.
guess = input("Guess a letter: ").lower()
print(guess)


#TODO-3 - Check if the letter the user guessed (guess) is one of the letter in the chosen_word. Print "right"
#is, "wrong" if it's not.
for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")'''

#****************************************************************************************************************
#Program2: Replacing blanks with guesses
'''* Create an empty string called placeholder.
* For each letter in the chosen_word add a _ to placeholder
* So if the chosen_word was 'Apple'. placeholder s each should be _ _ _ _ _ with 5 "_" representing each 
letter to guess.ExceptionGroup'''
'''word_list= ["Sourab","Aman","Ankit"]

chosen_word = random.choice(word_list) 
print(chosen_word)

# TODO-1: Create a "Placeholder" with the same number of blanks at the chosen_word
placeholder=""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder+="_"
print(placeholder)

guess=input("Guess a letter :").lower()
#TODO-2: Create a "display" that puta the guests letter in the right positions and _ in the rest of the string.
display=""

for letter in chosen_word:
    if letter == guess:
        display += letter
    else:
        display+="_"
print(display)'''

#****************************************************************************************************************************
#Program3: Checking if the player has won
word_list= ["Sourab","Aman","Ankit"]

chosen_word = random.choice(word_list).lower() 
print(chosen_word)

# TODO-1: Create a "Placeholder" with the same number of blanks at the chosen_word
placeholder=""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder+="_"
print(placeholder)
#TODO-2: Use a while loop to let the user gusess gain
game_over = False   # Initialize a flag that controls the game loop; False means the game is still running

correct_letters = []  # List to store letters the user has guessed correctly

while not game_over:  # Loop will continue running as long as game_over is False
    guess = input("Guess a letter :").lower()  # Ask the user to guess a letter, convert to lowercase for consistency

    display = ""  # Initialize an empty string to build the word with guessed letters and blanks

    # Loop through each letter in the chosen word
    for letter in chosen_word:
        if letter == guess:
            # If the current letter matches the user's guess:
            # - Add the guessed letter to the display
            # - Save the letter in correct_letters so we remember it
            display += letter
            correct_letters.append(guess)

        elif letter in correct_letters:
            # If the letter was guessed correctly in an earlier round:
            # - Show it in the display
            display += letter

        else:
            # If the letter hasn't been guessed yet:
            # - Show an underscore (_) instead
            display += "_"

    print(display)  # Show the user their progress (correct letters + underscores)

    if "_" not in display:
        game_over = True
        print("You Win!")

#*********************************************************************************************************

