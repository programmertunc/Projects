from words import words
import string
import random
#Clean up list remove '-' and spaces
new_list = words.copy()
dash = '-'
space =" "
for index, val in  enumerate(new_list):
    if dash in val:
        new_list[index] = val.replace(dash,"")
    if space in val:
        new_list[index] = val.replace(space,"")


def hangman():
    lives = 10
    random_word = random.choice(new_list) # a random word from list
    random_word_list = ["_"] * len(random_word)  #Create a list length of random_word acts as a placeholder for '_'
    guessed_letters = set() #Letters the user already guessed
    while lives > 0 and "_" in random_word_list:
        user_guess = input("Enter a letter").lower() #User guess
        

        if not user_guess.isalpha() or len(user_guess) != 1:
            print("Enter valid letter")
            continue
        if user_guess in guessed_letters:
            print("You already guessed that letter")
            continue

        guessed_letters.add(user_guess)


        if user_guess in random_word:
            for i,v in enumerate(random_word):
                if user_guess == v:
                    random_word_list[i] = v
            print("Correct")
        else:
            lives -= 1
            print(f"Wrong you have {lives} tries left")

        print("".join(random_word_list))

    if "_" not in random_word_list:
        print(f"You won word was {random_word}")
    else:
        print(f"You lost word was {random_word}")

hangman()













