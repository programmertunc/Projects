import random
print("Welcome to the Password Generator")

numbers=[0,1,2,3,4,5,6,7,8,9]

chars=[]
for i in range(65,91):
    chars.append(chr(i))
for i in range(97,123):
    chars.append(chr(i))

symbols=["@","!","'","^","#","$","&","(",")"]

user_input_numbers = int(input("Enter how many numbers you want"))
user_input_chars = int(input("Enter the number of characters"))
user_input_symbols = int(input("Enter the number of symbols"))
password=[]

for i in range(0,user_input_numbers):
    password.append(random.choice(numbers))

for i in range(0,user_input_chars):
    password.append(random.choice(chars))

for i in range(0,user_input_symbols):
    password.append(random.choice(symbols))
random.shuffle(password)
password = [str(i) for i in password]
print("You password is:\n"+''.join(password))

