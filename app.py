# app.py
# A simple Python program to greet the user and calculate sum of two numbers

def greet_user():
    name = input("Enter your name: ")
    print(f"Hello, {name}! Welcome to this Python program.\n")

def add_two_numbers():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        total = num1 + num2
        print(f"The sum of {num1} and {num2} is {total}.")
    except ValueError:
        print("Please enter valid nos")

def main():
    greet_user()
    add_two_numbers()

if __name__ == "__main__":
    main()
