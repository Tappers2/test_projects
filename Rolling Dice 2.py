#import random module
import random
#min 1 and max 6 as a normal 6 sided dice
min = 1
max = 6

#Explain the game
print ("Welcome to dice game.  You have up to 3 turns to roll 5 dice.  Enter 'y' or 'n' followed by pressing enter to record your choice")
print("From rolling the dice you want to get the highest scores possible.")
print("You want to get as many of the following as possible:","1","2","3","4","5","6",sep="\n")
print("You have up to 3 rolls per turn and can choose to keep as many dice as you want")

#start game
start = input("Press enter to start: ")

#start with 1st turn
turn = 1

#creating list for values
dice_values = []

#setting initial input value so dice is rolled
roll_again = "y"


#max of 3 turns
while turn <=3:
    if roll_again =="y" and turn <3:
        print ("This is roll " + str(turn))
        print ("Rolling the dice...")
        print ("The values are...")
        for i in range(5):
            dice_values = (random.randint(min,max))
            print (dice_values)
        turn = turn + 1
        roll_again = input("Roll the dice again?")
    elif roll_again == "y" and turn ==3:
        print ("This is your third and final roll for this turn")
        print ("Rolling the dice...")
        print ("The values are...")
        for i in range(5):
            dice_values = (random.randint(min,max))
            print (dice_values)
        turn = turn + 1       
    elif roll_again == "n":
        roll_again = input("Type 'n' again to confirm do not want to roll again or 'y' to roll again:")
        if roll_again == "n":
            break
        elif roll_again != "n":
            if roll_again =="y":
                print ("This is roll " + str(turn))
                print ("Rolling the dice...")
                print ("The values are...")
                for i in range(5):
                    print (random.randint(min,max))
                turn = turn + 1
                roll_again = input("Roll the dice again?")
    else:
        roll_again = input ("Please enter a permitted value 'y' or 'n':")

print ("You've had the maximum amount of rolls")
    
    