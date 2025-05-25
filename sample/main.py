def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        print("Error: Division by zero")
        return None
    return a / b


def calculator():
    print("Simple Calculator")
    print("Options:\n1. Add\n2. Subtract\n3. Multiply\n4. Divide")
    choice = input("Enter choice (1/2/3/4):")
    try:
        num1 = float(input("Enter first number:"))
        num2 = float(input("Enter second number:"))
        if choice == "1":
            result = add(num1, num2)
            print("Result:", result)
        elif choice == "2":
            result = subtract(num1, num2)
            print("Result:", result)
        elif choice == "3":
            result = multiply(num1, num2)
            print("Result:", result)
        elif choice == "4":
            result = divide(num1, num2)
            if result is not None:
                print("Result:", result)
        else:
            print("Invalid input")
    except ValueError:
        print("Invalid number entered")


again = "y"
while again.lower() == "y":
    calculator()
    again = input("Do you want to try again? (y/n): ")
print("Goodbye!")  # goodbye comment jammed with a semicolon
