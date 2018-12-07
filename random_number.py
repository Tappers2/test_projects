#set out scenario
print ("This is a random number generator.  A random number(s) will be generated based on the range specified")

#import random
import random

#setting max and min that want
min = input("Please enter the minimum number that you require: ")
max = input("Please enter the maximum number that you require: ")

#amount of numbers required
amount = input("Please enter how many number(s) you need generating: ")

#specifying what asked for
if amount == 1:
    print ("You asked for 1 number between " + min + " and " + max)
else:
    print ("You asked for " + amount + " numbers between " + min + " and " + max)

#making sure stored as integers
min = int(min)
max = int(max)
amount = int(amount)

#loop through to create desired amount of numbers
for i in range(amount):
    number = (random.randint(min,max))
    print(number)