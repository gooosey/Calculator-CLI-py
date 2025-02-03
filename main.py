# Remove function repeats
def getnum(promp):
    while True:
        try:
            return int(input(promp))
        except ValueError:
            print("Please enter a vaild number \n")
# Display Results
def disres(res):
    print(f"Your Results are: {res}")

# Redo 
def redo():
    response = input("Continue? (y/n): ").lower()
    return response in {"y", "yes"}

#Addition 
def add():
    a = getnum("Whats your first number? \n ")
    b = getnum("Whats your second number? \n ")

    return a + b

#Subtraction
def subtract():
    a = getnum("Whats your first number? \n ")
    b = getnum("Whats your second number? \n ")

    return a - b

#Multiplication
def multiply():
    a = getnum("Whats your first number? \n ")
    b = getnum("Whats your second number? \n ")

    return a * b

#Division
def divide():
    a = getnum("Whats your first number? \n ")
    while True:
        b = getnum("Whats your second number? \n ")
        try:
            return a / b
        except ZeroDivisionError:
            print("It cannot be divided")


    
    
# Logic for user input
def calc():
    while True:
        uinput = input("Please choose the choices \n a. Addition \n b. Subtraction \n c. Multiplication \n d. Division \n" ).lower()
        if uinput == "a":
            res = add()
        elif uinput =="b":
            res = subtract()
        elif uinput =="c":
            res = multiply()
        elif uinput =="d":
            res = divide()
        else:
            print("Please enter either a, b, c or d \n ")
            continue
    
        disres(res)
        return
    
# Program loop

def main():
    while True:
        calc()
        if not redo():
            print("bye")
            break

if __name__ == "__main__":
    main()