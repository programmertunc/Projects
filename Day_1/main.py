#Data Types
print(dir(str))

for i in dir(str): #exclude dunder methods
    if "__" not in i:
        print(i)

def my_Capitalize(string):
    first_char=string[0] 
    if ord(first_char) >= 97 and ord(first_char) <=122:
        store = ord(first_char) -32 #convert ascii
        char = chr(store)   #convert back to char
        new_string = char #assign capitilized char to new string
        for i in string:
            if i != string[0]: # if not first index 
                new_string +=  i # assign rest of string to new string 
    return new_string

#Not the best of implementations.I am doing this to understand better
name = "tunc"
print(name.capitalize())
print(my_Capitalize("tunc"))