#Day 35 of 100
   
#guess the number game in python
import random

chosen = random.randint(1,100)
print("Choose a number between 1 and 100")
while True:
    try:
    answer = int(input("Enter yout number: "))
    if (answer < chosen):
        print("your guess is SMALLER than the chosen number")
    elif (answer > chosen):
        print("your guess is BIGGER than the chosen number")
    else:
        print("Great! You guessed it right" +str(chosen))
        break
    except:
        print("Please enter a number only!")
        
