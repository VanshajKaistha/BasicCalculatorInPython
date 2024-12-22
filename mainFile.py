def mainMenu():
    print("***Main Menu****")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Increment")
    print("7. Decrement")
    print("0. Exit")
#------------------------------------------------------------------------------------#

while 1:
    mainMenu();

#------------------------------------------------------------------------------------#
def add():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = num1 + num2
    print("The sum of the two numbers is:", result)
#------------------------------------------------------------------------------------#
def sub():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = num1 - num2
    print("The sub of the two numbers is:", result)
#------------------------------------------------------------------------------------#
def multiply():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = num1 * num2
    print("The multiplication of the two numbers is:", result)
#------------------------------------------------------------------------------------#
def divide():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = num1/num2
    print("The divided value of the two numbers is:", result)
#------------------------------------------------------------------------------------#
def mod():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = num1%num2
    print("The mod of the two numbers is:", result)
#------------------------------------------------------------------------------------#
def increment():
    num1 = float(input("Enter first number: "))
    result = num1++
    print("The incremented number is:", result)
#------------------------------------------------------------------------------------#
