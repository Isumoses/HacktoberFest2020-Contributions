import random
import pyttsx3
import os

eng=pyttsx3.init()
eng.setProperty("rate",125)

roll_die=lambda : random.randint(1,6)

def dice_game(rounds):
    eng.say("Enter the name of player 1")
    eng.runAndWait()
    player01=input("Enter the name :")
    
    eng.say("Enter the name of player 2")
    eng.runAndWait()
    player02=input("Enter the name :")
    
    p1win=0
    p2win=0
    rn=1
    
    eng.say("Let's start")
    eng.runAndWait()
    
    while rn<=rounds:
        if rn!=1:
            input("Please just press ENTER key to continue the game")
        
        eng.say("Round number {}".format(rn))
        eng.runAndWait()
        p1=roll_die()
        p2=roll_die()
        print("Player 1 roll: {} & Player 2 roll: {}".format(p1,p2))
        
        if p1==p2:
            print("Round was drawn")
        elif p1>p2:
            print("Round was won by {}".format(player01))
            p1win+=1
        else:
            print("Round was won by {}".format(player02))
            p2win+=1
        
        rn+=1
        print("*******************************************************************************************")
    if p1win==p2win:
        eng.say("Game was drawn")
        eng.runAndWait()
    elif p1win>p2win:
        print("Congratulations {}. You have won.".format(player01))
        eng.say("Game was won by {}. You have won, {} rounds out of {}".format(player01,p1win,rounds))
        eng.runAndWait()
    else:
        print("Congratulations {}. You have won.".format(player02))
        eng.say("Game was won by {}. You have won, {} rounds out of {}".format(player02,p2win,rounds))
        eng.runAndWait()
