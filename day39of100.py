#day 39 of 100
#Hangman - Pyhton project 
#a game where user has to guess words, and chaces if fails to guess then less the chances to solve 

#pip install random
import random as rd 
from collections import Counter

secretwords= '''school, coffe, coding, ayushi, alisha , aditi, anglyn, kite,brother, friends, bunny, naina, home, college '''
secretwords = secretwords.split(' ')
word = rd.choice(secretwords)

if __name__ == "__main__":
    print("Guess the words! hint: back to memory lane!")
    for i in word:
        print("_", end= " ")
        print()
        
        
        playing = True
        correctletter = ' '
        chances = len(word)+ 2
        correct= 0
        wrong = 0
    try:
        while chances !=0 and wrong == 0:
            print()
            chances-=1
            
            try:
                guess= str(input("enter a word: "))
            except: 
                print("enter only one letter!")
                continue
            if not guess.isalpha():
                print("enter only a letter!")
                continue
            elif len(guess) >1:
                print("Enter Single letter on a time")
                
            elif guess in correctletter:
                print("you have already entered this letter")
                
                
            if guess in word:
                i = word.count(guess)
            for _ in range(i):
                correctletter +=guess
                
            for char in word:
                
                if char in correctletter and (Counter(correctletter) != Counter(word)):
                    print(char, end = ' ')
                    correct += 1
                    
                elif (Counter(correctletter) == Counter(word)):
                    print("The word is: ", end=' ')
                    print(word)
                    wrong = 1
                    print('Congratulations, You won!')
                    break 
                    
                else:
                    print('_', end = ' ')
                    
        if chances <= 0 and (Counter(correctletter) != Counter(word)):
            print()
            print('You lost! Try again..')
            print('The word was {}'.format(word))
  
    except KeyboardInterrupt:
        print()
        print('sorry! Try again.')
        exit()
                
        
            