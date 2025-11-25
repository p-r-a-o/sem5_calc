#!/usr/bin/env python3
def add(a, b):
    """Add two numbers"""
    return a + b

def subtract(a, b):
    """Subtract second number from first"""
    return a - b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

def divide(a, b):
    """Divide first number by second"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def get_number(prompt):
    """Get a valid number from user input"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def display_menu():
    """Display calculator menu"""
    print("\n" + "="*40)
    print("  SIMPLE CALCULATOR")
    print("="*40)
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")
    print("="*40)

def main():
    """Main calculator loop"""
    print("Welcome to Simple Calculator!")
    
    while True:
        display_menu()
        
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == '5':
            print("\nThank you for using Simple Calculator. Goodbye!")
            break
        
        if choice not in ['1', '2', '3', '4']:
            print("\nInvalid choice. Please select 1-5.")
            continue
        
        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")
        
        try:
            if choice == '1':
                result = add(num1, num2)
                operation = "+"
            elif choice == '2':
                result = subtract(num1, num2)
                operation = "-"
            elif choice == '3':
                result = multiply(num1, num2)
                operation = "*"
            elif choice == '4':
                result = divide(num1, num2)
                operation = "/"
            
            print(f"\nResult: {num1} {operation} {num2} = {result}")
        
        except ValueError as e:
            print(f"\nError: {e}")
        except Exception as e:
            print(f"\nAn unexpected error occurred: {e}")

if __name__ == "__main__":
    main()