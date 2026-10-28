"""Simple command-line calculator.

Supports addition, subtraction, multiplication, and division.
Run with: python calculator.py
"""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


def get_number(prompt):
    """Keep asking until the user enters a valid number."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")


def format_number(value):
    """Show whole numbers without the trailing .0"""
    return int(value) if value == int(value) else round(value, 10)


def main():
    operations = {
        "1": ("+", add),
        "2": ("-", subtract),
        "3": ("*", multiply),
        "4": ("/", divide),
    }

    print("=== Python Calculator ===")

    while True:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("\nEnter choice (1-5): ").strip()

        if choice == "5":
            print("Goodbye!")
            break

        if choice not in operations:
            print("Invalid choice. Please select 1-5.")
            continue

        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        symbol, func = operations[choice]

        try:
            result = func(num1, num2)
            print(
                f"Result: {format_number(num1)} {symbol} "
                f"{format_number(num2)} = {format_number(result)}"
            )
        except ZeroDivisionError as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()
