import random
import os
#import sys

from game_data import sports_data
from game_data import actors_data 

from art import vs
from art import logo

def assign():
    return random.choice(sports_data)

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
    person1 = assign()
    person2 = assign()

    print(person1)
    print(person2)


user_choice = input("Start Game(y/n)\n")

if user_choice =='y':
    os.system('cls')
    higher_lower()
elif user_choice =='n':
    print("Exiting!")
else: 
    print("Invalid Input.")

    