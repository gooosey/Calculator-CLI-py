import time

#Addition 
def add():
    a = int(input("Whats your first number? \n"))
    b = int(input("What your second number? \n"))
    res = a + b
    print(f"Your results are: {res}")
    time.sleep(3)
    again = input("would you like to go again?").lower()
    if again == "y" or again == "yes":
        calc()
    else: 
        print("Have a great day...")  

#Subtraction
def subtract():
    a = int(input("Whats your first number? \n"))
    b = int(input("What your second number? \n"))
    res = a - b
    print(f"Your results are: {res}")
    time.sleep(3)
    again = input("would you like to go again?").lower()
    if again == "y" or again == "yes":
        calc()
    else: 
        print("Have a great day...")  

#Multiplication
def multiply():
    a = int(input("Whats your first number? \n"))
    b = int(input("What your second number? \n"))
    res = a * b
    print(f"Your results are: {res}")
    time.sleep(3)
    again = input("would you like to go again?").lower()
    if again == "y" or again == "yes":
        calc()
    else: 
        print("Have a great day...")  

#Division
def divide():
    a = int(input("Whats your first number? \n"))
    b = int(input("What your second number? \n"))
    
    # Avoid 0/0
    try:
        res = a / b
    except ZeroDivisionError:
        return print("This number is undefined")

    print(f"Your results are: {res}")
    time.sleep(3)
    again = input("would you like to go again?").lower()
    if again == "y" or again == "yes":
        calc()
    else: 
        print("Have a great day...")  

# Logic for user input
def calc():
    uinput = input("Please choose the choices \n a. Addition \n b. Subtraction \n c. Multiplication \n d. Division \n" ).lower()
    if uinput == "a":
        add()
    elif uinput =="b":
        subtract()
    elif uinput =="c":
        multiply()
    elif uinput =="d":
        divide()
    else:
        print("Please enter either a, b, c or d \n ")
        calc()

calc()
