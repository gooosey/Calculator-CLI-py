import time

# Helper functions
def get_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter an integer.")

def display_result(res):
    print(f"Result: {res}")
    time.sleep(1)

def ask_again():
    response = input("Continue? (y/n): ").lower()
    return response in {"y", "yes"}

# Operations
def add():
    a = get_number("First number: ")
    b = get_number("Second number: ")
    return a + b

def subtract():
    a = get_number("First number: ")
    b = get_number("Second number: ")
    return a - b

def multiply():
    a = get_number("First number: ")
    b = get_number("Second number: ")
    return a * b

def divide():
    a = get_number("First number: ")
    while True:
        b = get_number("Second number: ")
        try:
            return a / b
        except ZeroDivisionError:
            print("Error: Division by zero. Try again.")

# Main logic
def main():
    operations = {
        "a": ("Addition", add),
        "b": ("Subtraction", subtract),
        "c": ("Multiplication", multiply),
        "d": ("Division", divide)
    }

    while True:
        choice = input(
            "Choose an operation:\n"
            "a. Addition\n"
            "b. Subtraction\n"
            "c. Multiplication\n"
            "d. Division\n"
            "> ").lower()

        if choice not in operations:
            print("Invalid choice. Please pick a, b, c, or d.")
            continue

        operation_name, func = operations[choice]
        print(f"{operation_name} selected.")
        result = func()
        display_result(result)

        if not ask_again():
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()