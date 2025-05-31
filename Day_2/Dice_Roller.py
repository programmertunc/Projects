import random
print("Welcome to the Dice Roller program")
user_input= 1
while(user_input != 0):
    random_choice = random.randint(1,6)
    print("You rolled :",random_choice)
    user_input= int(input("Enter 1 to roll again ,Enter 0 to exit"))
