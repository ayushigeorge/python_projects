#Day 34 of 100 days of code
# Python project name : Mad Libs Generator
#~Game Description~
#In this user has to enter some words for generating a story, for which they have already choosed the title for!
pip install tkinter as Tk
from tkinter import *

root = Tk()
root.title("Day 34 Mad Libs Generator")
root.geometry('400x400')
root.config(bg="Blue")
Label(root, text='Python_project day 34 of 100 Mad Libs Generator').place(x=100, y=20)

Story1Button = Button(root, text=' Story to tell', font=("Times New Roman", 13),command=lambda: Story1(Screen),bg='Blue')
Story1Button.place(x=140, y=90)
Story2Button = Button(root text='think above limits', font=("Times New Roman", 13),command=lambda: Story2(Screen), bg='Blue')
Story2Button.place(x=150, y=150)
 
Screen.update()
Screen.mainloop()

def Story1(win):
  def final(tl: Toplevel, name, age, City, place, book, food):
 
    text = f'''
       Me and {name} of {age}, decided to plan a trip to {City} and visit {place}.
       we took the map and went to our adventure, where we acquire knowledge through {book}.
       
       We really enjoyed {food}! We are looking forward to go again and enjoy '''
 
    tl.geometry(newGeometry='500x550')
 
    Label(tl, text='Story:',  wraplength=tl.winfo_width()).place(x=160, y=310)
    Label(tl, text=text,wraplength=tl.winfo_width()).place(x=0, y=330)
 
  NewScreen = Toplevel(win, bg='grey')
  NewScreen.title("New day, new story")
  NewScreen.geometry('500x500')
  Label(NewScreen, text='Day highlights').place(x=100, y=0)
  Label(NewScreen, text='Name:').place(x=0, y=35)
  Label(NewScreen, text='Enter a game:').place(x=0, y=70)
  Label(NewScreen, text='Enter a city:').place(x=0, y=110)
  Label(NewScreen, text='Enter the name of a player:').place(x=0, y=150)
  Label(NewScreen, text='Enter the name of a drink:').place(x=0, y=190)
  Label(NewScreen, text='Enter the name of a snack:').place(x=0, y=230)
  Name = Entry(NewScreen, width=17)
  Name.place(x=250, y=35)
  game = Entry(NewScreen, width=17)
  game.place(x=250, y=70)
  city = Entry(NewScreen, width=17)
  city.place(x=250, y=105)
  player = Entry(NewScreen, width=17)
  player.place(x=250, y=150)
  drink = Entry(NewScreen, width=17)
  drink.place(x=250, y=190)
  snack = Entry(NewScreen, width=17)
  snack.place(x=250, y=220)
  SubmitButton = Button(NewScreen, text="Submit", background="Blue", font=('Times', 12), command=lambda:final(NewScreen, Name.get(), game.get(), city.get(), player.get(), drink.get(), snack.get()))
  SubmitButton.place(x=150, y=270)
 
  NewScreen.mainloop()
  def Story2(win):
    def final(tl: Toplevel, profession, noun, feeling, emotion,verb):
            text = f'''
            One day me and my friend {name} decided to play a {sports} game in {City}.
       But we were not able to play. So, we went to the game and watched our favourite player {playername}.
       We drank {drinkname} and also ate some {snacks} 
       We really enjoyed it! We are looking forward to go again and enjoy 
'''
 
            tl.geometry(newGeometry='500x550')
 
            Label(tl, text='Story:',  wraplength=tl.winfo_width()).place(x=160, y=310)
            Label(tl, text=text,wraplength=tl.winfo_width()).place(x=0, y=330)
    NewScreen = Toplevel(win, bg='red')
    NewScreen.title("Ambitions")
    NewScreen.geometry('500x500')
    Label(NewScreen, text='Ambitions').place(x=150, y=0)
    Label(NewScreen, text='Enter a profession:').place(x=0, y=35)
    Label(NewScreen, text='Enter a noun:').place(x=0, y=70)
    Label(NewScreen, text='Enter a feeling:').place(x=0, y=110)
    Label(NewScreen, text='Enter a emotion:').place(x=0, y=150)
    Label(NewScreen, text='Enter a verb:').place(x=0, y=190)
    Profession = Entry(NewScreen, width=17)
    Profession.place(x=250, y=35)
    Noun = Entry(NewScreen, width=17)
    Noun.place(x=250, y=70)
    Feeling = Entry(NewScreen, width=17)
    Feeling.place(x=250, y=105)
    Emotion= Entry(NewScreen, width=17)
    Emotion.place(x=250, y=150)
    Verb = Entry(NewScreen, width=17)
    Verb.place(x=250, y=190)
    SubmitButton = Button(NewScreen, text="Submit", background="Blue", font=('Times', 12), command=lambda:final(NewScreen, Profession.get(), Noun.get(), Feeling.get(), Emotion.get(), Verb.get()))
    SubmitButton.place(x=150, y=270)
    NewScreen.mainloop