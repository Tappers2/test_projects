import random

#rolling dice
def dice(num):
    dice = []
    for i in range(num):
        dice.append(random.randint(1,6))
    return dice

#first roll
def roll_one():
    print("Rolling the dice to start turn.  The values are...")
    first = dice(5)
    print(first)
    return first

#second roll
def roll_two(first):
#    print(first)
    print("Which dice do you want to take forward to the next turn?  Please enter their numeric position.  If you wish to keep no dice press enter")
    keep_index = input("> ")
    keep_index = list(map(int,keep_index.split()))
    keep_index = list(map(lambda x: x-1, keep_index))
    number = 5 -(len(keep_index))
#    print(number)
#    print (keep_index)
    keep_dice=[]
    second = dice(number)
    for i in keep_index:
        keep_dice.append(first[i])
    print("You've kept " , keep_dice)
    print("Second roll.  Dice are: ")
    keep_dice = keep_dice + second
    print(keep_dice)
    second = keep_dice
#    return keep_dice
#    print(second)
    return second

#third roll
def roll_three(second):
    print("Which dice do you want to take forward to the next turn?  Please enter their numeric position.  If you wish to keep no dice press enter")
    keep_index = []
    keep_index = input("> ")
    keep_index = list(map(int,keep_index.split()))
    keep_index = list(map(lambda x: x-1, keep_index))
    number = 5 -(len(keep_index))
#    print(number)
#    print (keep_index)
    keep_dice =[]
    third = dice(number)
    for i in keep_index:
        keep_dice.append(second[i])    
    print("You've kept" , keep_dice)
    print("Third and final roll for this turn.  Dice are: ")
    keep_dice = keep_dice + third
    print(keep_dice)
    roll = keep_dice
    return roll

turn = roll_three(roll_two(roll_one()))
