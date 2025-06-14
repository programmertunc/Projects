# freecodecamp - 12 Beginner Python Projects Coding Course

import random
import math
from words import words
import string

"""
list_a = [1,2,3,4,5,"abc",True]
for k,v in enumerate(list_a):
    print(k+1,v)
    
str_a = "Hello"
new_str = ""
length = len(str_a) -1
while length >= 0:
    new_str += str_a[length]
    length -= 1
print(new_str)

str_a = "Hello"
new_str = str_a[::-1]
print(new_str)

str_a = "Hello"
new_str = "".join(reversed(str_a))
print(new_str)

str_a = "Hello"
str_list = list(str_a)
l = 0
r = len(str_a) -1
while l < r:
    str_list[r], str_list[l] = str_list[l], str_list[r]
    l += 1
    r -= 1
str_a = ''.join(str_list) 
print(str_a)



youtuber = "Kyli Ying"

print("subscribe to " + youtuber)
print("subscirbe to {}".format(youtuber))
print(f"subscribe to {youtuber}")



adj = input("Enter an adjective")
verb_1 = input("Enter a verb")
verb_2 = input("Enter a verb")
famous_person = input("Enter a famous person")


madlib = f"Computer programming is so {adj}\I love to {verb_1}\Stay hydrated and {verb_2} like you are {famous_person}"
print(madlib)


list_a = [1,2,3,4,5,6,7,8,9,10]
print([i+1 for i in list_a])
print([i*i for i in list_a])
c = [i*i for i in list_a]
print(c)

set_a = {"apple","banana","cherry"}
list_a = list(set_a)
d = [i.upper() for i in list_a]
print(d)


def guess(x):
    comp_choice = random.randint(1,x)
    lives = 5
    while lives > 0:
        user_choice = int(input("Enter a number between 1-x inclusive"))
        if user_choice == comp_choice:
            print("You Won!")
            break
        if abs(comp_choice - user_choice) >= 10:
            print("COLD")
        elif abs(comp_choice - user_choice) < 10 and abs(comp_choice - user_choice) >= 5:
            print("Warm")
        elif abs(comp_choice - user_choice) <5:
            print("Warmer")
        lives -= 1
        print(f"You have {lives} lives left")
    print("Game over you lost")
    print(f"Number was {comp_choice}")

guess(5)


def play():
    user_choice = input("Enter 'r' for rock 'p' for paper 's' for scissors")
    comp_choice = random.choice(['r','p','s'])

    if user_choice == comp_choice:
        return "Tie"
    
    if is_win(user_choice,comp_choice):
        return "You Won"
    return "You Lost"

def is_win(player,opponent):
    if (player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r') or (player == 's' and opponent == 'p'):
        return True

"""
