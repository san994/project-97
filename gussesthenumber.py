import random 
import time

num = random.randint(1,9)
numberofgusses = 0

while (numberofgusses<=5):
    inp = int(input("enter a number between 1-9: "))
    timeofday = time.strftime('%d/%H:%M:%S')
    print("time={}           gussesremain {}".format(timeofday,5-numberofgusses))
    numberofgusses+=1

    if(inp==num):
        print("YOU WON!")
        break
    elif(inp>num):
        print("{} number is greater".format(inp))
    elif(inp<num):
        print("{} number is smaller".format(inp))
    elif(inp=="quit"):
        print("BYE BYE")
        break
if(numberofgusses>=5):
    print("gameOver")