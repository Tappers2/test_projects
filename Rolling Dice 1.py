import random
min = 1
max = 6

roll_again = "yes"

while roll_again =="yes" or roll_again =="y" or roll_again =="Y":
    print ("Rolling the dice...")
    print ("The values is...")
    print (random.randint(min,max))
    
    roll_again = input("Roll the dice again?")
    