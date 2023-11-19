import random
import os

from game_data import sports_data
from game_data import actors_data 

from art import vs
from art import logo

def assign():
    temp = 2
    if temp == 1:
        return random.choice(sports_data)
    elif temp == 2:
        return random.choice(actors_data)
    
def compare(p1,p2,user_ans):
    followers1 = p1['follower_count']
    followers2 = p2['follower_count']

    ans = ''
    
    if followers1 > followers2:
        ans = p1['name']
    elif followers2 > followers1:
        ans = p2['name']
    
    if ans == user_ans:
        return True
    else:
        return False

def higher_lower():

    playing_game = True
    while(playing_game):
        score = 0
        guessing = True
        while(guessing):

            os.system('cls')
            print(logo)
            #category = input("Choose the category\n 1.Sports\n 2.Film\n")
            person1 = assign()
            person2 = assign()
            while(person1 == person2):
                person2 = assign()

            print(f"Name: {person1['name']}, Desc: {person1['description']}")
            print(vs)
            print(f"Name: {person2['name']}, Desc: {person2['description']}")

            user_ans = input("Enter Your Answer:")
            if compare(person1,person2,user_ans):
                score+= 1
                print("Current Score: ", score)
            else:
                print("You got it Wrong!")
                guessing = False
            
            play_again = input("Continue(y/n)\n")
            if play_again == 'y':
                continue
            elif play_again == 'n':
                playing_game = False
                os.system('cls')
                print("Your Score: ",score)
                print("Game Exited Successfully!")
            else:
                print("Invalid Input")
                playing_game = False


user_choice = input("Start Game(y/n)\n")

if user_choice == 'y':
    os.system('cls')
    higher_lower()
elif user_choice == 'n':
    print("Exiting!")
else: 
    print("Invalid Input.")

    