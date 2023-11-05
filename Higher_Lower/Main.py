import random
import os

from game_data import sports_data
from game_data import actors_data 

from art import vs
from art import logo

def assign(category):
    temp = 1
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

    print(logo)
    category = input("Choose the category\n 1.Sports\n 2.Film\n")
    person1 = assign(category)
    person2 = assign(category)
    #while(person1 == person2):
    #   person2 = assign()

    print(f"Name: {person1['name']}, Desc: {person1['description']}")
    print(vs)
    print(f"Name: {person2['name']}, Desc: {person2['description']}")

user_choice = input("Start Game(y/n)\n")

if user_choice == 'y':
    os.system('cls')
    higher_lower()
elif user_choice == 'n':
    print("Exiting!")
else: 
    print("Invalid Input.")

    