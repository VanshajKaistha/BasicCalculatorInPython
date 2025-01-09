#------------------------------------------------------------------------------------#
def add():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = num1 + num2
    print("The sum of the two numbers is:", result)
    return result
#------------------------------------------------------------------------------------#
def sub():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = num1 - num2
    print("The sub of the two numbers is:", result)
    return result
#------------------------------------------------------------------------------------#
def multiply():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = num1 * num2
    print("The multiplication of the two numbers is:", result)
    return result
#------------------------------------------------------------------------------------#
def divide():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = num1/num2
    print("The divided value of the two numbers is:", result)
    return result
#------------------------------------------------------------------------------------#
def mod():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = num1%num2
    print("The mod of the two numbers is:", result)
    return result
#------------------------------------------------------------------------------------#
def increment():
    num1 = float(input("Enter first number: "))
    result = num1+1
    print("The incremented number is:", result)
    return result
#------------------------------------------------------------------------------------#
def decrement():
    num1 = float(input("Enter first number: "))
    result = num1-1
    print("The decremented number is:", result)
    return result
#------------------------------------------------------------------------------------#
def exitFunc():#didnt used it yet could be used
    print("Exiting Calculator")
    return 
#------------------------------------------------------------------------------------#
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
    choice = int(input("Enter the operation you want to perform: "))

    if choice == 1:
        add()
    elif choice == 2:
         sub()
    elif choice == 3:
         multiply()
    elif choice == 4:
         divide()
    elif choice == 5:
         mod()
    elif choice == 6:
         increment()
    elif choice == 7:
         decrement()
    elif choice == 0:
         exit("""Exiting Calculator.
Visit again :)""")
#------------------------------------------------------------------------------------#

while 1:
    mainMenu();

