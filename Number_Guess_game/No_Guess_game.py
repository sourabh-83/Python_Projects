from random import randint

Easy_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# Function to check users "guess against actual answer"
def check_answer(user_guess, actual_answer, turns):
    '''Checks answer guess, returns the number of turns remaining.'''
    if user_guess > actual_answer:
        print("Too High")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too Low")
        return turns - 1
    else:
        print(f"You got it! The answer was {actual_answer}")

# Funstion to set difficult

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard':")
    if level == "easy":
        return Easy_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    # Choosing a random number between 1 and 100.
    print("Welcome to the Number Gusessing Game!")
    print("I'm thinking of a numner between 1 and 100")
    answer = randint(1,100)
    print(f"The Correct answer is {answer}")
    
    turns = set_difficulty()

# Repeat the guessing functionality if they get it wrong
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number")
        # Let the user guess a number
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guess, You lose")
            return
        elif guess != answer:
            print("GUess again")
#Track the numnber of turns and return by 1 if they get it wrong
game()

    
    
    
#Ouput:
# You Choose hard
'''Welcome to the Number Gusessing Game!
I'm thinking of a numner between 1 and 100 
The Correct answer is 27
Choose a difficulty. Type 'easy' or 'hard':hard
You have 5 attempts remaining to guess the number
Make a guess: 56
Too High
GUess again
You have 4 attempts remaining to guess the number
Make a guess: 66
Too High
GUess again
You have 3 attempts remaining to guess the number
Make a guess: 77
Too High
GUess again
You have 2 attempts remaining to guess the number
Make a guess: 88
Too High
GUess again
You have 1 attempts remaining to guess the number
Make a guess: 99
Too High
You've run out of guess, You lose'''

#You Choose easy
'''Welcome to the Number Gusessing Game!
I'm thinking of a numner between 1 and 100 
The Correct answer is 86
Choose a difficulty. Type 'easy' or 'hard':easy
You have 10 attempts remaining to guess the number
Make a guess: 56
Too Low
GUess again
You have 9 attempts remaining to guess the number
Make a guess: 45
Too Low
GUess again
You have 8 attempts remaining to guess the number
Make a guess: 55
Too Low
GUess again
You have 7 attempts remaining to guess the number
Make a guess: 56
Too Low
GUess again
You have 6 attempts remaining to guess the number
Make a guess: 45
Too Low
GUess again
You have 5 attempts remaining to guess the number
Make a guess: 55
Too Low
GUess again
You have 4 attempts remaining to guess the number
Make a guess: 50
Too Low
GUess again
You have 3 attempts remaining to guess the number
Make a guess: 45
Too Low
GUess again
You have 2 attempts remaining to guess the number
Make a guess: 54
Too Low
GUess again
You have 1 attempts remaining to guess the number
Make a guess: 44
Too Low
You've run out of guess, You lose'''


