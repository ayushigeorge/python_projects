# DAY 33 of 100 days of code
#basic Adventure Game in python



answer = input("Lets Play an Adventure game! Comment yes/no: \n").lower().strip()

if answer =="yes":
    print("you are about take a flight to france, it got hijacked!!")
    choice = input("\t would you a)jump off the plane /b)fight the hijackers?\n")
    
    if choice=="a":
        print("you died\n")
        print("game over!")
    else:
        print("you survied and went to recieve a medal from government, but your car crashed in way,\n")
        choice= input("\t a)would you take lift/ b)save other passengers (who helped you to fight)")
        if choice=="a":
            print("you found no lift instead got mugged!\n")
            print("game over!")
        else:
            print("\tthe other passengers repaired the car after aid, they calculated the amount to be recieved and decided to kill you!\t ")
            choice = input("\ta) be nice to them, b)pick a fight\n ")
            if choice=="a":
                print("you got killed, Game over!\n")
            else:
                print("Yay!\t you won and got all the honor, medal and prize\n")
                print("game over!")
else:
    print("invalid choice \n")
        