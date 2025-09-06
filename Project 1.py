'''Write a project to implemnet a "Snake, Water, Gun" game where the user
plays against the computer. zzzzzzzuse 's' for Snake,'w' for Water, and 'g' for Gun.in
    The game should continue until the user decides to stop. Display who wins each round'''

import random
computer=random.choice([-1,0,1])
while True:
    youStr=input("Enter your choice:")
    youDict={"s":1,"w":-1,"g":0}    
    reverseDict={1:"Snake",-1:"Water",0:"Gun"}
    you=youDict[youStr]
    print(f"You choose {reverseDict[you]}\nComputer choose {reverseDict[computer]}")
    if(computer==you):
        print("Its draw")
    else:
        if(computer==-1 and you==1):
            print("you Win!")
        elif(computer==-1 and you==0):
            print("you loss!")
        elif(computer ==1 and you==-1):
            print("you win!")
        elif(computer==1 and you==0):
            print("you loss!")
        elif(computer==0 and you==1):
            print("you win!")
        elif(computer==0 and you==1):
            print("you loss!")
        else:
            print("Something wen wrong")
        repeat = input("Do you want to play again? (Yes/No): ").strip().lower()
        if repeat == "no":
            break