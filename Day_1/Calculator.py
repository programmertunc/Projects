print("Welcome to the Calculator App")
print("Enter 'y' or 'Y' to exit program")
print(" '+' for addition")
print(" '-' for subtraction")
print(" '*' for multiplication")
print(" '/' for division")
print(" '%' for modulus")
print(" '**' for power")

while(1):
    operand_1 = float(input("Enter first number"))
    operand_2 = float(input("Enter second number"))
    operator = input("Enter operator symbol")

    if operator == "+":
        print(operand_1 + operand_2 )
    elif operator == "-":
        print(operand_1 - operand_2 )
    elif operator == "*":
        print(operand_1 * operand_2 )
    elif operator == "/":
        print(operand_1 / operand_2 )
    elif operator == "%":
        print(operand_1 % operand_2 )
    elif operator == "**":
        print(operand_1 ** operand_2 )
    else:
        print("Wrong input.")
    program_running= input("Enter y or Y to exit program")
    if program_running.casefold() == "y":
        break



